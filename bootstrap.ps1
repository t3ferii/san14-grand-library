# Standalone entrypoint: Windows PowerShell 5.1+, no Git/Python/JDK installation needed.
param([string]$GamePath = '', [string]$CacheRoot = '', [switch]$Doctor)
$ErrorActionPreference = 'Stop'
if (-not $CacheRoot) { $CacheRoot = Join-Path $env:LOCALAPPDATA 'San14GrandLibrary' }
$CacheRoot = [IO.Path]::GetFullPath($CacheRoot)
if ($CacheRoot -match '[()!%&^]') { throw 'Select -CacheRoot without ()!%&^.' }
[void][IO.Directory]::CreateDirectory($CacheRoot)
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$archiveName = 'source-' + [Guid]::NewGuid().ToString('N') + '.zip'
$zip = Join-Path $CacheRoot ('downloads/' + $archiveName)
if ((Test-Path -LiteralPath (Split-Path -Parent $zip)) -and ((Get-Item -LiteralPath (Split-Path -Parent $zip) -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Source download directory is a reparse point.' }
[void][IO.Directory]::CreateDirectory((Split-Path -Parent $zip))
if (Test-Path -LiteralPath $zip) { throw 'Source archive already exists; refusing to overwrite.' }
Invoke-WebRequest -Uri 'https://github.com/t3ferii/san14-grand-library/archive/refs/heads/main.zip' -OutFile ($zip + '.part') -UseBasicParsing
Move-Item -LiteralPath ($zip + '.part') -Destination $zip -Force
$hash = (Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash.Substring(0,16).ToLowerInvariant()
$source = Join-Path $CacheRoot ('source/' + $hash)
if (-not (Test-Path -LiteralPath (Join-Path $source 'san14-grand-library-main/prepare.ps1'))) {
    Expand-Archive -LiteralPath $zip -DestinationPath $source -Force
}
$prepare = Join-Path $source 'san14-grand-library-main/prepare.ps1'
. (Join-Path (Split-Path -Parent $prepare) 'tools/python_runtime.ps1')
Register-San14Archive -CacheRoot $CacheRoot -Relative ('downloads/' + $archiveName) -Kind 'source_archive' -Name 'source' -Sha256 ((Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash.ToLowerInvariant()) -CreatedByCaller
$prepareArgs = @{ CacheRoot = $CacheRoot }
if ($GamePath) { $prepareArgs.GamePath = $GamePath }
if ($Doctor) { $prepareArgs.Doctor = $true }
& $prepare @prepareArgs
Write-Output ('Library source: ' + (Split-Path -Parent $prepare))
