from __future__ import annotations

import json
import subprocess
import tempfile
import zipfile
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

REPOSITORY = "SojaIntegral/AQWHelper"
LATEST_RELEASE_URL = f"https://api.github.com/repos/{REPOSITORY}/releases/latest"
ARCHIVE_URL = f"https://github.com/{REPOSITORY}/archive/refs/tags/"
MAX_ARCHIVE_SIZE = 50 * 1024 * 1024


class NoPublishedReleaseError(Exception):
    pass


def install_latest_release(
    python_executable: str | Path,
    *,
    timeout: float = 20.0,
) -> str:
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

    archive_url = f"{ARCHIVE_URL}{quote(tag, safe='')}.zip"
    archive_request = Request(archive_url, headers={"User-Agent": "AQWHelper"})
    with tempfile.TemporaryDirectory(prefix="aqwhelper-update-") as directory:
        archive_path = Path(directory) / "release.zip"
        size = 0
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

    return tag
