from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

from linux_console.platform_utils import is_windows

REPOSITORY = "SojaIntegral/AQWHelper"
LATEST_RELEASE_URL = f"https://api.github.com/repos/{REPOSITORY}/releases/latest"
ARCHIVE_URL = f"https://github.com/{REPOSITORY}/archive/refs/tags/"
MAX_ARCHIVE_SIZE = 50 * 1024 * 1024


class NoPublishedReleaseError(Exception):
    pass


def latest_release_tag(timeout: float = 20.0) -> str:
    request = Request(
        LATEST_RELEASE_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "AQWHelper",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            release: object = json.loads(response.read(64 * 1024).decode("utf-8"))
    except HTTPError as error:
        if error.code == 404:
            raise NoPublishedReleaseError(
                "No published GitHub release was found for AQW Helper."
            ) from error
        raise

    if not isinstance(release, dict):
        raise ValueError("GitHub returned invalid release information.")
    tag = release.get("tag_name")
    if not isinstance(tag, str) or not tag.strip() or len(tag) > 200:
        raise ValueError("GitHub returned an invalid release tag.")
    return tag


def _download_and_verify_release(timeout: float = 20.0) -> tuple[str, Path]:
    """Download and verify the latest release.
    
    Returns:
        Tuple of (tag, archive_path) where archive_path is in a temporary directory.
    """
    tag = latest_release_tag(timeout)
    archive_url = f"{ARCHIVE_URL}{quote(tag, safe='')}.zip"
    archive_request = Request(archive_url, headers={"User-Agent": "AQWHelper"})
    temp_dir = Path(tempfile.mkdtemp(prefix="aqwhelper-update-"))
    archive_path = temp_dir / "release.zip"
    size = 0
    try:
        with urlopen(archive_request, timeout=timeout) as response:
            with archive_path.open("wb") as archive_file:
                while chunk := response.read(64 * 1024):
                    size += len(chunk)
                    if size > MAX_ARCHIVE_SIZE:
                        raise ValueError("The release archive exceeds the 50 MiB limit.")
                    archive_file.write(chunk)

        if size == 0 or not zipfile.is_zipfile(archive_path):
            raise ValueError("GitHub returned an invalid release archive.")
        with zipfile.ZipFile(archive_path) as archive:
            if archive.testzip() is not None:
                raise ValueError("The release archive failed its integrity check.")
    except Exception:
        shutil.rmtree(temp_dir)
        raise

    return tag, archive_path


def install_latest_release(
    python_executable: str | Path,
    *,
    timeout: float = 20.0,
) -> str:
    """Install the latest release.
    
    On Linux: Installs directly in place.
    On Windows: Schedules installation to avoid file locking issues.
    """
    tag, archive_path = _download_and_verify_release(timeout=timeout)
    
    if is_windows():
        _install_release_windows(python_executable, archive_path, tag)
    else:
        try:
            _install_release_unix(python_executable, archive_path, tag)
        finally:
            shutil.rmtree(archive_path.parent)
    
    return tag


def _install_release_unix(
    python_executable: str | Path,
    archive_path: Path,
    tag: str,
) -> None:
    """Install release on Unix-like systems (immediate installation)."""
    try:
        subprocess.run(
            [
                str(python_executable),
                "-m",
                "pip",
                "install",
                "--upgrade",
                "--force-reinstall",
                str(archive_path),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
    except subprocess.CalledProcessError as error:
        detail = (error.stderr or error.stdout or str(error)).strip()
        raise RuntimeError(f"Could not install release {tag}: {detail}") from error
    except subprocess.TimeoutExpired as error:
        raise TimeoutError(f"Installing release {tag} timed out.") from error


def _install_release_windows(
    python_executable: str | Path,
    archive_path: Path,
    tag: str,
) -> None:
    """Install release on Windows (with scheduled deferred installation).
    
    On Windows, we create a helper script that will be run after the app exits
    to avoid file locking issues during pip upgrade.
    """
    # Create a temporary PowerShell script that will run the installation
    script_path = archive_path.parent / "install_update.ps1"
    
    # Escape paths for PowerShell
    archive_path_ps = str(archive_path).replace("'", "''")
    python_exe_ps = str(python_executable).replace("'", "''")
    
    script_content = f"""
# AQW Helper Update Script for Windows
$ArchivePath = '{archive_path_ps}'
$PythonExe = '{python_exe_ps}'

try {{
    & $PythonExe -m pip install --upgrade --force-reinstall $ArchivePath -q
    if ($LASTEXITCODE -ne 0) {{ throw "pip exited with code $LASTEXITCODE" }}
    Remove-Item -Force -Path $ArchivePath -ErrorAction SilentlyContinue
    Write-Host "AQW Helper has been updated to {tag}." -ForegroundColor Green
}} catch {{
    Write-Host "Failed to update AQW Helper: $_" -ForegroundColor Red
    exit 1
}}
"""
    
    script_path.write_text(script_content, encoding="utf-8")
    
    # Create a batch file that runs the PowerShell script in a new window
    batch_path = script_path.with_suffix(".bat")
    batch_content = f"""@echo off
REM AQW Helper Update Batch Script
REM Give the app a moment to exit so pip can replace its files.
timeout /t 3 /nobreak >nul
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "{script_path}"
pause
"""
    batch_path.write_text(batch_content, encoding="utf-8")
    
    # start reads its first quoted argument as the window title, so pass an
    # empty one before the path.
    try:
        subprocess.Popen(
            ["cmd", "/c", "start", "", str(batch_path)],
            shell=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except OSError as error:
        raise RuntimeError(
            f"Could not start the update. Run {batch_path} to finish it."
        ) from error
