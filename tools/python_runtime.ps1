# Shared by preparation and queries. Existing Python is never modified or uninstalled.
function Resolve-San14Python {
    param([string]$CacheRoot, [string]$RepoRoot, [switch]$AllowInstall)
    $deps = Get-Content -LiteralPath (Join-Path $RepoRoot 'tools/dependencies.lock.json') -Raw | ConvertFrom-Json
    $managedRoot = Join-Path $CacheRoot ('tools/python-' + $deps.python.version)
    $managedExe = Join-Path $managedRoot 'python.exe'
    $candidates = @()
    if ($env:SAN14_PYTHON) { $candidates += $env:SAN14_PYTHON }
    foreach ($name in @('python.exe', 'python3.exe', 'python', 'python3', 'py.exe')) {
        $command = Get-Command $name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($command) { $candidates += $command.Source }
    }
    $candidates += $managedExe
    $existing = Find-San14InstalledPython -Candidates $candidates
    if ($existing) { return $existing }
    if (-not $AllowInstall) { throw 'Python 3.12+ unavailable. Run .\prepare.ps1 first.' }
    if (Test-Path -LiteralPath $managedRoot) { throw 'Existing Python directory is unusable; preserved. Select another cache root.' }
    [void][IO.Directory]::CreateDirectory($CacheRoot)
    # Serializes Python bootstrap before the Python-level preparation lock can exist.
    $bootstrapLock = [IO.File]::Open((Join-Path $CacheRoot 'python-bootstrap.lock'), 'OpenOrCreate', 'ReadWrite', 'None')
    try {
        if (Test-Path -LiteralPath $managedExe) { return $managedExe }
        foreach ($managedParent in @((Join-Path $CacheRoot 'downloads'), (Join-Path $CacheRoot 'tools'))) {
            if ((Test-Path -LiteralPath $managedParent) -and ((Get-Item -LiteralPath $managedParent -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Managed tool parent is a reparse point.' }
        }
        $archive = Join-Path $CacheRoot 'downloads/python.zip'
        [void][IO.Directory]::CreateDirectory((Split-Path -Parent $archive))
        if (Test-Path -LiteralPath $archive) {
            if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant() -ne $deps.python.sha256) {
                throw 'Existing Python archive changed; preserved. Select another cache root.'
            }
        } else {
            Register-San14Archive -CacheRoot $CacheRoot -Relative 'downloads/python.zip' -Kind 'archive' -Name 'python' -Sha256 $deps.python.sha256
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
            Invoke-WebRequest -Uri $deps.python.url -OutFile ($archive + '.part') -UseBasicParsing
            if ((Get-FileHash -LiteralPath ($archive + '.part') -Algorithm SHA256).Hash.ToLowerInvariant() -ne $deps.python.sha256) { throw 'Python download SHA256 mismatch.' }
            Move-Item -LiteralPath ($archive + '.part') -Destination $archive
        }
        Write-Host ('Preparing query Python ' + $deps.python.version)
        Expand-Archive -LiteralPath $archive -DestinationPath $managedRoot
        # Python is the query runtime and is intentionally outside the tool cleanup allowlist.
        return $managedExe
    } finally { $bootstrapLock.Dispose() }
}

function Find-San14InstalledPython {
    param([string[]]$Candidates)
    $oldAutomatic = [Environment]::GetEnvironmentVariable('PYTHON_MANAGER_AUTOMATIC_INSTALL', 'Process')
    $oldLegacy = [Environment]::GetEnvironmentVariable('PYLAUNCHER_ALLOW_INSTALL', 'Process')
    try {
        # New Python managers can install runtimes on first launch. Discovery is read-only.
        [Environment]::SetEnvironmentVariable('PYTHON_MANAGER_AUTOMATIC_INSTALL', 'false', 'Process')
        [Environment]::SetEnvironmentVariable('PYLAUNCHER_ALLOW_INSTALL', $null, 'Process')
        $probe = 'import sys,json,sqlite3,zlib,hashlib;sys.exit(2) if sys.version_info < (3,12) else print(json.dumps(dict(executable=sys.executable,version=chr(46).join(map(str,sys.version_info[:3])))))'
        foreach ($candidate in ($Candidates | Select-Object -Unique)) {
            if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) { continue }
            if ($candidate -match '[\\/]Microsoft[\\/]WindowsApps[\\/]') { continue }
            $runtimes = @($candidate)
            if ([IO.Path]::GetFileName($candidate) -eq 'py.exe') {
                $runtimes = @()
                try {
                    $listing = & $candidate -0p 2>$null
                    if ($LASTEXITCODE -eq 0) {
                        foreach ($line in $listing) {
                            if ($line -match '([A-Za-z]:[\\/].*[\\/]python\.exe)\s*$') { $runtimes += $Matches[1] }
                        }
                    }
                } catch { continue }
            }
            foreach ($executable in $runtimes) {
                try {
                    if (-not (Test-Path -LiteralPath $executable -PathType Leaf)) { continue }
                    $probeText = & $executable -X utf8 -I -c $probe 2>$null
                    if ($LASTEXITCODE -ne 0) { continue }
                    $runtime = ($probeText -join "`n") | ConvertFrom-Json
                    if ($runtime.executable -and (Test-Path -LiteralPath $runtime.executable -PathType Leaf)) { return [string]$runtime.executable }
                } catch { continue }
            }
        }
    } finally {
        [Environment]::SetEnvironmentVariable('PYTHON_MANAGER_AUTOMATIC_INSTALL', $oldAutomatic, 'Process')
        [Environment]::SetEnvironmentVariable('PYLAUNCHER_ALLOW_INSTALL', $oldLegacy, 'Process')
    }
}

function Register-San14Archive {
    param([string]$CacheRoot, [string]$Relative, [string]$Kind, [string]$Name, [string]$Sha256, [switch]$CreatedByCaller)
    if ($Sha256 -notmatch '^[0-9a-f]{64}$') { throw 'Invalid archive checksum.' }
    if ($Kind -eq 'archive') {
        if ($Name -notin @('python','java','ghidra','steamless') -or $Relative -cne ('downloads/' + $Name + '.zip')) { throw 'Invalid managed archive path.' }
    } elseif ($Kind -eq 'source_archive') {
        if ($Name -cne 'source' -or $Relative -cnotmatch '^downloads/source-[0-9a-f]{32}\.zip$') { throw 'Invalid source archive path.' }
    } else { throw 'Unsupported archive kind.' }
    $recordRoot = Join-Path $CacheRoot '.owned'
    if ((Test-Path -LiteralPath $recordRoot) -and ((Get-Item -LiteralPath $recordRoot -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Ownership directory is a reparse point.' }
    [void][IO.Directory]::CreateDirectory($recordRoot)
    $hasher = [Security.Cryptography.SHA256]::Create()
    try { $key = -join ($hasher.ComputeHash([Text.Encoding]::UTF8.GetBytes($Relative)) | ForEach-Object { $_.ToString('x2') }) }
    finally { $hasher.Dispose() }
    $recordPath = Join-Path $recordRoot ($key + '.json')
    $record = @{ schema = 1; cache_root = [IO.Path]::GetFullPath($CacheRoot); relative = $Relative; kind = $Kind; name = $Name; version = ''; sha256 = $Sha256 }
    if (Test-Path -LiteralPath $recordPath) {
        if ((Get-Item -LiteralPath $recordPath -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Ownership record is a reparse point.' }
        $saved = Get-Content -LiteralPath $recordPath -Raw | ConvertFrom-Json
        if ($saved.sha256 -ne $Sha256 -or $saved.relative -ne $Relative -or $saved.kind -ne $Kind) { throw 'Archive ownership record differs; preserved.' }
        return
    }
    if (-not $CreatedByCaller -and (Test-Path -LiteralPath (Join-Path $CacheRoot $Relative))) { return }
    [IO.File]::WriteAllText(($recordPath + '.tmp'), ($record | ConvertTo-Json), (New-Object Text.UTF8Encoding($false)))
    Move-Item -LiteralPath ($recordPath + '.tmp') -Destination $recordPath
}
