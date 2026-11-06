from __future__ import annotations

from importlib.resources import files
import re

from linux_console.release_update import NoPublishedReleaseError, latest_release_tag


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
    # Compare against the release /update would install, not main's VERSION.
    try:
        latest_version = latest_release_tag(timeout).strip().removeprefix("v")
    except NoPublishedReleaseError:
        return False
    if re.fullmatch(r"\d+(?:\.\d+)*", latest_version) is None:
        raise ValueError("The latest release tag is not a version number.")

    return _parse(latest_version) > _parse(installed_version)


def _parse(version: str) -> tuple[int, ...]:
    parts = [int(part) for part in version.split(".")]
    while len(parts) > 1 and parts[-1] == 0:
        parts.pop()
    return tuple(parts)
