from __future__ import annotations

from importlib.resources import files
import re
from urllib.request import urlopen

REMOTE_VERSION_URL = (
    "https://raw.githubusercontent.com/SojaIntegral/AQWHelper/main/"
    "src/linux_console/VERSION"
)


def update_available(timeout: float = 3.0) -> bool:
    current_version = (
        files("linux_console").joinpath("VERSION").read_text(encoding="ascii").strip()
    )
    if not current_version:
        raise ValueError("The installed application version is empty.")

    with urlopen(REMOTE_VERSION_URL, timeout=timeout) as response:
        latest_version = response.read(64).decode("ascii").strip()
    if not latest_version:
        raise ValueError("The remote application version is empty.")
    if re.fullmatch(r"\d+(?:\.\d+)*", latest_version) is None:
        raise ValueError("The remote application version is invalid.")

    return latest_version != current_version
