param([Parameter(ValueFromRemainingArguments=$true)][string[]]$QueryArgs)
$ErrorActionPreference = 'Stop'
$cacheRoot = if ($env:SAN14_LIBRARY_CACHE) { $env:SAN14_LIBRARY_CACHE } else { Join-Path $env:LOCALAPPDATA 'San14GrandLibrary' }
$deps = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'tools/dependencies.lock.json') -Raw | ConvertFrom-Json
$python = Join-Path $cacheRoot ('tools/python-' + $deps.python.version + '/python.exe')
if (-not (Test-Path -LiteralPath $python)) { throw 'Run .\prepare.ps1 first.' }
$env:SAN14_LIBRARY_CACHE = $cacheRoot
& $python -X utf8 -I (Join-Path $PSScriptRoot 'tools/library.py') @QueryArgs
exit $LASTEXITCODE
