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
. (Join-Path $repoRoot 'tools/python_runtime.ps1')
$pythonExe = Resolve-San14Python -CacheRoot $CacheRoot -RepoRoot $repoRoot -AllowInstall
# Isolated embedded Python deliberately ignores global packages, PYTHONPATH and sitecustomize.
$argsList = @('-X', 'utf8', '-I', (Join-Path $repoRoot 'tools/library.py'), 'prepare', '--cache-root', $CacheRoot)
if ($GamePath) { $argsList += @('--game', $GamePath) }
if ($Doctor) { $argsList += '--doctor' }
if ($VerifyOnly) { $argsList += '--verify-only' }
if ($ReuseExport) { $argsList += @('--reuse-export', $ReuseExport) }
& $pythonExe @argsList
if ($LASTEXITCODE -ne 0) { throw "Preparation failed (exit $LASTEXITCODE). See the path printed above." }
