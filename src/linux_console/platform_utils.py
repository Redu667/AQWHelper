"""Platform-specific utilities for Windows/Linux compatibility.

This module abstracts platform differences while keeping Linux code untouched.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def get_config_directory() -> Path:
    """Get the appropriate config directory for the current platform.
    
    Linux: XDG_CONFIG_HOME or ~/.config
    Windows: %APPDATA%\AQW Helper
    """
    if sys.platform.startswith("win"):
        # Windows
        appdata = os.environ.get("APPDATA")
        if not appdata:
            # Fallback to user home
            return Path.home() / "AppData" / "Roaming" / "AQW Helper"
        return Path(appdata) / "AQW Helper"
    else:
        # Linux/Unix
        config_home = Path(
            os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config"
        )
        return config_home


def get_bin_directory() -> Path:
    """Get the appropriate bin directory for the current platform.
    
    Linux: ~/.local/bin
    Windows: Script directory in venv or user AppData\Local\bin
    """
    if sys.platform.startswith("win"):
        # Windows: use AppData\Local\bin or Scripts from venv
        local_appdata = os.environ.get("LOCALAPPDATA")
        if not local_appdata:
            local_appdata = str(Path.home() / "AppData" / "Local")
        return Path(local_appdata) / "AQW Helper" / "bin"
    else:
        # Linux
        return Path.home() / ".local" / "bin"


def get_desktop_shortcuts_directory() -> Path | None:
    """Get the desktop shortcuts directory for the current platform.
    
    Windows: %USERPROFILE%\Desktop
    Linux: ~/Desktop (if it exists)
    
    Returns None if the directory doesn't exist and shouldn't be created.
    """
    if sys.platform.startswith("win"):
        # Windows
        desktop = Path.home() / "Desktop"
        return desktop
    else:
        # Linux
        desktop = Path.home() / "Desktop"
        if desktop.exists():
            return desktop
        return None


def is_windows() -> bool:
    """Check if the current platform is Windows."""
    return sys.platform.startswith("win")


def is_linux() -> bool:
    """Check if the current platform is Linux."""
    return sys.platform.startswith("linux")


def get_star_chars() -> tuple[str, str]:
    """Get star characters appropriate for the current platform.
    
    Linux: Uses full Unicode stars (★ ☆)
    Windows: Uses ASCII equivalents (*,-) that display reliably in CMD
    
    Returns: (filled_star, hollow_star)
    """
    if sys.platform.startswith("win"):
        # Windows CMD has limited Unicode support, use ASCII
        return ("*", "-")
    else:
        # Linux terminal has full Unicode support
        return ("★", "☆")
