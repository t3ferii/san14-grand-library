# Standalone entrypoint: Windows PowerShell 5.1+, no Git/Python/JDK installation needed.
param([string]$GamePath = '', [string]$CacheRoot = '', [switch]$Doctor)
$ErrorActionPreference = 'Stop'
if (-not $CacheRoot) { $CacheRoot = Join-Path $env:LOCALAPPDATA 'San14GrandLibrary' }
$CacheRoot = [IO.Path]::GetFullPath($CacheRoot)
if ($CacheRoot -match '[()!%&^]') { throw 'Select -CacheRoot without ()!%&^.' }
[void][IO.Directory]::CreateDirectory($CacheRoot)
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$zip = Join-Path $CacheRoot 'library-source.zip'
Invoke-WebRequest -Uri 'https://github.com/t3ferii/san14-grand-library/archive/refs/heads/main.zip' -OutFile ($zip + '.part') -UseBasicParsing
Move-Item -LiteralPath ($zip + '.part') -Destination $zip -Force
$hash = (Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash.Substring(0,16).ToLowerInvariant()
$source = Join-Path $CacheRoot ('source/' + $hash)
if (-not (Test-Path -LiteralPath (Join-Path $source 'san14-grand-library-main/prepare.ps1'))) {
    Expand-Archive -LiteralPath $zip -DestinationPath $source -Force
}
$prepare = Join-Path $source 'san14-grand-library-main/prepare.ps1'
$prepareArgs = @{ CacheRoot = $CacheRoot }
if ($GamePath) { $prepareArgs.GamePath = $GamePath }
if ($Doctor) { $prepareArgs.Doctor = $true }
& $prepare @prepareArgs
Write-Output ('Library source: ' + (Split-Path -Parent $prepare))
