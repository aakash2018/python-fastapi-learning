<#
PowerShell script to create a virtual environment and install dependencies.
Run from repository root or from `backend` folder.
#>

$venvPath = Join-Path -Path (Get-Location) -ChildPath ".venv"
if (-Not (Test-Path $venvPath)) {
    python -m venv $venvPath
}

Write-Host "Activating venv and installing requirements..."
& "$venvPath\Scripts\Activate.ps1"
python -m pip install --upgrade pip
pip install -r "$(Split-Path -Path $MyInvocation.MyCommand.Definition -Parent)\requirements.txt"

Write-Host "Virtual environment ready at $venvPath"
