param(
    [string]$GamePath = '',
    [string]$CacheRoot = '',
    [switch]$Doctor,
    [switch]$VerifyOnly,
    [string]$ReuseExport = ''
)
$ErrorActionPreference = 'Stop'
if (-not [Environment]::Is64BitOperatingSystem) { throw 'Windows x64 required.' }
if (-not $CacheRoot) { $CacheRoot = Join-Path $env:LOCALAPPDATA 'San14GrandLibrary' }
$CacheRoot = [IO.Path]::GetFullPath($CacheRoot)
if ($CacheRoot -match '[()!%&^]') { throw 'Use -CacheRoot with a path without ()!%&^ for the Ghidra batch launcher.' }
[void][IO.Directory]::CreateDirectory($CacheRoot)
$repoRoot = $PSScriptRoot
$deps = Get-Content -LiteralPath (Join-Path $repoRoot 'tools/dependencies.lock.json') -Raw | ConvertFrom-Json
$pythonRoot = Join-Path $CacheRoot ('tools/python-' + $deps.python.version)
$pythonExe = Join-Path $pythonRoot 'python.exe'
$archive = Join-Path $CacheRoot 'downloads/python.zip'
if (-not (Test-Path -LiteralPath $pythonExe)) {
    [void][IO.Directory]::CreateDirectory((Split-Path -Parent $archive))
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    if (-not (Test-Path -LiteralPath $archive) -or (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant() -ne $deps.python.sha256) {
        $part = $archive + '.part'
        Invoke-WebRequest -Uri $deps.python.url -OutFile $part -UseBasicParsing
        if ((Get-FileHash -LiteralPath $part -Algorithm SHA256).Hash.ToLowerInvariant() -ne $deps.python.sha256) { throw 'Python download SHA256 mismatch.' }
        Move-Item -LiteralPath $part -Destination $archive -Force
    }
    Expand-Archive -LiteralPath $archive -DestinationPath $pythonRoot -Force
}
# Isolated embedded Python deliberately ignores global packages, PYTHONPATH and sitecustomize.
$argsList = @('-X', 'utf8', '-I', (Join-Path $repoRoot 'tools/library.py'), 'prepare', '--cache-root', $CacheRoot)
if ($GamePath) { $argsList += @('--game', $GamePath) }
if ($Doctor) { $argsList += '--doctor' }
if ($VerifyOnly) { $argsList += '--verify-only' }
if ($ReuseExport) { $argsList += @('--reuse-export', $ReuseExport) }
& $pythonExe @argsList
if ($LASTEXITCODE -ne 0) { throw "Preparation failed (exit $LASTEXITCODE). See the path printed above." }
