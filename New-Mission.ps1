<#
.SYNOPSIS
  Create a new mission repository from this template.
.EXAMPLE
  .\New-Mission.ps1 -Name "My-Mission"
  .\New-Mission.ps1 -Name "Board-Campaign" -Destination "D:\Missions"
#>
param(
    [Parameter(Mandatory = $true)][string]$Name,
    [string]$Destination = (Split-Path -Parent $PSScriptRoot)
)
$ErrorActionPreference = 'Stop'
$target = Join-Path $Destination $Name
if (Test-Path $target) { throw "Target already exists: $target" }

# Copy everything except the template's git history
New-Item -ItemType Directory -Path $target | Out-Null
Get-ChildItem -LiteralPath $PSScriptRoot -Force |
    Where-Object { $_.Name -ne '.git' } |
    ForEach-Object { Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force }

git -C $target init --quiet
git -C $target add -A
git -C $target commit --quiet -m "Start mission $Name from Mission-Template"
if ($LASTEXITCODE -ne 0) {
    Write-Warning "Files copied to $target, but the first git commit failed (is git user.name/user.email set?). Fix that, then run: git -C `"$target`" commit -m `"Start mission $Name`""
    exit 1
}
Write-Host "Mission repository created: $target"
Write-Host "Next: open it in Claude Code and fill in MISSION.md."
