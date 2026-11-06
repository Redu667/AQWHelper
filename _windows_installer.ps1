#Requires -RunAsAdministrator

# Check if Python is installed
$pythonCheck = python --version 2>&1
if (-not $?) {
    Write-Host "Python not found. Downloading and installing Python..."
    
    $pythonUrl = "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe"
    $pythonInstaller = "$env:TEMP\python-installer.exe"
    
    # Download Python
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller -ErrorAction Stop
    
    # Install Python with PATH added and wait for the installer to finish
    Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    
    # Clean up installer
    Remove-Item $pythonInstaller -Force
    
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

Write-Host "Python is installed: $pythonCheck"

$AppDataPath = Join-Path $env:APPDATA "AQW Helper"
$VenvPath = Join-Path $AppDataPath ".venv"

New-Item -ItemType Directory -Path $AppDataPath -Force | Out-Null

Write-Host "Creating virtual environment..."
python -m venv $VenvPath
if (-not $?) { Write-Error "Failed to create venv"; exit 1 }

Write-Host "Installing pip and dependencies..."
& "$VenvPath\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel
if (-not $?) { Write-Error "Failed to install pip tools"; exit 1 }

& "$VenvPath\Scripts\python.exe" -m pip install textual colorama
if (-not $?) { Write-Error "Failed to install textual and colorama"; exit 1 }

$projectPath = Split-Path -Parent $PSCommandPath
Write-Host "Installing app from $projectPath..."
& "$VenvPath\Scripts\python.exe" -m pip install -e $projectPath
if (-not $?) { Write-Error "Failed to install app"; exit 1 }

$shell = New-Object -ComObject WScript.Shell
$desktop = [Environment]::GetFolderPath("Desktop")

# Create shortcut with UTF-8 environment variable
$shortcut = $shell.CreateShortcut("$desktop\AQW Helper.lnk")
$shortcut.TargetPath = "cmd.exe"
$shortcut.Arguments = "/k chcp 65001 >nul && set PYTHONIOENCODING=utf-8 && cd /d `"$VenvPath`" && Scripts\activate.bat && python -m linux_console.app"
$shortcut.WorkingDirectory = $VenvPath
$shortcut.WindowStyle = 1
$shortcut.Save()

Write-Host "Installation complete"
