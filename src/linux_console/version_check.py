from __future__ import annotations

from importlib.resources import files
import re
from urllib.request import Request, urlopen

REMOTE_VERSION_URL = (
    "https://raw.githubusercontent.com/SojaIntegral/AQWHelper/main/"
    "src/linux_console/VERSION"
)


def current_version() -> str:
    version = (
        files("linux_console").joinpath("VERSION").read_text(encoding="ascii").strip()
    )
    if not version:
        raise ValueError("The installed application version is empty.")
    if re.fullmatch(r"\d+(?:\.\d+)*", version) is None:
        raise ValueError("The installed application version is invalid.")
    return version


def update_available(timeout: float = 3.0) -> bool:
    installed_version = current_version()
    request = Request(
        REMOTE_VERSION_URL,
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "AQWHelper",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        latest_version = response.read(64).decode("ascii").strip()
    if not latest_version:
        raise ValueError("The remote application version is empty.")
    if re.fullmatch(r"\d+(?:\.\d+)*", latest_version) is None:
        raise ValueError("The remote application version is invalid.")

    return _parse(latest_version) > _parse(installed_version)


def _parse(version: str) -> tuple[int, ...]:
    parts = [int(part) for part in version.split(".")]
    while len(parts) > 1 and parts[-1] == 0:
        parts.pop()
    return tuple(parts)
