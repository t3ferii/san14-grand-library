param([Parameter(ValueFromRemainingArguments=$true)][string[]]$QueryArgs)
$ErrorActionPreference = 'Stop'
$cacheRoot = if ($env:SAN14_LIBRARY_CACHE) { $env:SAN14_LIBRARY_CACHE } else { Join-Path $env:LOCALAPPDATA 'San14GrandLibrary' }
. (Join-Path $PSScriptRoot 'tools/python_runtime.ps1')
$python = Resolve-San14Python -CacheRoot $cacheRoot -RepoRoot $PSScriptRoot
$env:SAN14_LIBRARY_CACHE = $cacheRoot
& $python -X utf8 -I (Join-Path $PSScriptRoot 'tools/library.py') @QueryArgs
exit $LASTEXITCODE
