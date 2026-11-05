@echo off
REM AQW Helper Windows Installer Wrapper
REM This batch file launches the PowerShell installer script

setlocal enabledelayedexpansion

REM Check if running as Administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo.
    echo ERROR: This installer must be run as Administrator
    echo.
    echo Please right-click on this file and select "Run as administrator"
    echo.
    pause
    exit /b 1
)

REM Get the directory where this script is located
cd /d "%~dp0"

REM Launch the PowerShell installer
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "_windows_installer.ps1" %*

if %errorlevel% neq 0 (
    echo.
    echo Installation failed. Press any key to exit...
    pause
    exit /b 1
)

exit /b 0
