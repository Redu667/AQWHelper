import contextlib
import json
import os
import re
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from linux_console.platform_utils import get_config_directory, is_windows


CHARACTER_PAGE_URL = "https://account.aq.com/CharPage"
USER_AGENT = "AQW-Helper/0.1"
DEFAULT_ENHANCEMENTS = (
    "Fighter",
    "Wizard",
    "Healer",
    "Thief",
    "Hybrid",
    "Spellbreaker",
    "Lucky",
)
ENHANCEMENT_ADDONS = (
    "Awe Blast",
    "Spiral Carve",
    "Mana Vamp",
    "Health Vamp",
    "Powerword DIE",
)
AVAILABLE_ENHANCEMENTS = (
    "Forge",
    "Vim",
    "Examen",
    "Anima",
    "Pneuma",
    "Hearty",
    "Absolution",
    "Vainglory",
    "Avarice",
    "Penitence",
    "Lament",
    "Lacerate",
    "Smite",
    "Praxis",
    "Acheron",
    "Hero's Valiance",
    "Elysium",
    "Arcana's Concerto",
    "Dauntless",
    "Ravenous",
    *ENHANCEMENT_ADDONS,
)
TOGGLEABLE_ENHANCEMENTS = tuple(
    name for name in AVAILABLE_ENHANCEMENTS if name not in ENHANCEMENT_ADDONS
)
REMOVED_ENHANCEMENTS = ("Awe",)


def config_path() -> Path:
    config_home = get_config_directory()
    if not is_windows():
        _move_files_from_config_root(config_home)
    return config_home / "config.json"


def _move_files_from_config_root(config_home: Path) -> None:
    # Versions 1.1 to 1.5 saved profiles straight into ~/.config. Only files
    # with this app's exact keys are moved. profiles.json goes last so an
    # interrupted move is retried, and a failed move never stops the app.
    root = config_home.parent
    old_profiles = root / "profiles.json"
    old = _read_json(old_profiles)
    if not _is_profile_data(old):
        return
    with contextlib.suppress(OSError):
        characters = config_home / "characters"
        characters.mkdir(parents=True, exist_ok=True)
        for path in (root / "characters").glob("*.json"):
            character = _read_json(path)
            if isinstance(character, dict) and set(character) == {"account", "enhancements"}:
                path.replace(characters / path.name)
        with contextlib.suppress(OSError):
            (root / "characters").rmdir()

        new_profiles = config_home / "profiles.json"
        current = _read_json(new_profiles)
        if _is_profile_data(current):
            moved = {name.casefold() for name in old["profiles"]}
            profiles = [
                name for name in current["profiles"] if name.casefold() not in moved
            ] + old["profiles"]
            _write_profiles(
                new_profiles, profiles, old["last_used"] or current["last_used"]
            )
            old_profiles.unlink()
        else:
            old_profiles.replace(new_profiles)


def _is_profile_data(data: Any) -> bool:
    return (
        isinstance(data, dict)
        and set(data) == {"last_used", "profiles"}
        and isinstance(data["profiles"], list)
        and all(isinstance(name, str) for name in data["profiles"])
    )


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return None


def profile_data_path(settings_path: Path) -> Path:
    return settings_path.parent / "profiles.json"


def _normalize_profile_names(profiles: list[str]) -> list[str]:
    unique_profiles: list[str] = []
    seen: set[str] = set()
    for profile in profiles:
        normalized = profile.strip()
        folded = normalized.casefold()
        if folded not in seen:
            unique_profiles.append(normalized)
            seen.add(folded)
    return unique_profiles


def _write_profiles(path: Path, profiles: list[str], last_used: str | None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "last_used": last_used,
                "profiles": profiles,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def load_profiles(settings_path: Path) -> tuple[list[str], str | None]:
    path = profile_data_path(settings_path)
    try:
        data: Any = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        data = None
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {path}: {error}") from error

    if data is None:
        try:
            settings: Any = json.loads(settings_path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            settings = {}
        except json.JSONDecodeError as error:
            raise ValueError(
                f"Invalid JSON in settings {settings_path}: {error}"
            ) from error
        if not isinstance(settings, dict):
            raise ValueError("The saved AQW Helper settings are not a JSON object.")

        legacy_profiles = settings.get("account_history", [])
        if not isinstance(legacy_profiles, list) or any(
            not isinstance(profile, str) or not profile.strip()
            for profile in legacy_profiles
        ):
            raise ValueError("The saved profile list is invalid.")
        legacy_last_used = settings.get("account")
        if legacy_last_used is not None and (
            not isinstance(legacy_last_used, str) or not legacy_last_used.strip()
        ):
            raise ValueError("The saved last-used profile is invalid.")
        profiles = _normalize_profile_names(legacy_profiles)
        if legacy_last_used:
            last_used = legacy_last_used.strip()
            profiles = [
                profile
                for profile in profiles
                if profile.casefold() != last_used.casefold()
            ]
            profiles.append(last_used)
        else:
            last_used = None
        _write_profiles(path, profiles, last_used)

        if "account" in settings or "account_history" in settings:
            settings.pop("account", None)
            settings.pop("account_history", None)
            settings_path.write_text(
                json.dumps(settings, indent=2) + "\n",
                encoding="utf-8",
            )
        return profiles, last_used


    if not isinstance(data, dict):
        raise ValueError("The saved profile data is not a JSON object.")
    profiles = data.get("profiles")
    if not isinstance(profiles, list) or any(
        not isinstance(profile, str) or not profile.strip() for profile in profiles
    ):
        raise ValueError("The saved profile list is invalid.")

    profiles = _normalize_profile_names(profiles)
    last_used = data.get("last_used")
    if last_used is not None and (
        not isinstance(last_used, str) or not last_used.strip()
    ):
        raise ValueError("The saved last-used profile is invalid.")
    if isinstance(last_used, str):
        last_used = last_used.strip()
        if last_used.casefold() not in {profile.casefold() for profile in profiles}:
            raise ValueError("The last-used profile is missing from the profile list.")
    if not profiles and last_used is not None:
        raise ValueError(
            "Last-used profile cannot be set when the profile list is empty."
        )
    return profiles, last_used


def save_profile(settings_path: Path, profile: str) -> tuple[list[str], str]:
    normalized = profile.strip()
    if not normalized:
        raise ValueError("Profile name cannot be empty.")
    profiles, _ = load_profiles(settings_path)
    profiles = [
        saved for saved in profiles if saved.casefold() != normalized.casefold()
    ]
    profiles.append(normalized)
    _write_profiles(profile_data_path(settings_path), profiles, normalized)
    return profiles, normalized


def character_enhancements_path(settings_path: Path, account: str) -> Path:
    filename = quote(account.strip().casefold(), safe="") or "character"
    return settings_path.parent / "characters" / f"{filename}.json"


def load_character_enhancements(settings_path: Path, account: str) -> set[str]:
    path = character_enhancements_path(settings_path, account)
    try:
        character: Any = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return set(TOGGLEABLE_ENHANCEMENTS)

    saved_account = character.get("account") if isinstance(character, dict) else None
    if not isinstance(saved_account, str) or saved_account.casefold() != (
        account.strip().casefold()
    ):
        raise ValueError(f"Saved character settings for {account} are invalid.")

    selected = character.get("enhancements")
    if not isinstance(selected, list) or any(
        not isinstance(name, str)
        or name not in AVAILABLE_ENHANCEMENTS + REMOVED_ENHANCEMENTS
        for name in selected
    ):
        raise ValueError(f"Saved enhancements for {account} are invalid.")
    if len(set(selected)) != len(selected):
        raise ValueError(f"Saved enhancements for {account} contain duplicates.")
    return set(selected).intersection(TOGGLEABLE_ENHANCEMENTS)


def save_character_enhancements(
    settings_path: Path,
    account: str,
    selected: set[str],
) -> None:
    invalid = selected.difference(TOGGLEABLE_ENHANCEMENTS)
    if invalid:
        raise ValueError(f"Unknown enhancement selection: {', '.join(sorted(invalid))}")

    path = character_enhancements_path(settings_path, account)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "account": account.strip(),
                "enhancements": [
                    name for name in TOGGLEABLE_ENHANCEMENTS if name in selected
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def remove_profile(settings_path: Path, profile: str) -> bool:
    normalized_name = profile.strip().casefold()
    if not normalized_name:
        raise ValueError("Profile name cannot be empty.")
    profiles, last_used = load_profiles(settings_path)
    profile_file = profile_data_path(settings_path)
    remaining = [saved for saved in profiles if saved.casefold() != normalized_name]
    removed = len(remaining) != len(profiles)
    if not removed:
        return False

    if last_used and last_used.casefold() == normalized_name:
        last_used = remaining[-1] if remaining else None
    _write_profiles(profile_file, remaining, last_used)
    enhancement_path = character_enhancements_path(settings_path, profile)
    if enhancement_path.exists():
        enhancement_path.unlink()
    return True


def _fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8")


def fetch_classes(account: str) -> list[str]:
    account = account.strip()
    if not account:
        raise ValueError("Enter an AQW character name.")

    page_url = f"{CHARACTER_PAGE_URL}?{urlencode({'id': account})}"
    page = _fetch_text(page_url)
    character_id = re.search(r"\bvar\s+ccid\s*=\s*(\d+)\s*;", page)
    if character_id is None:
        raise ValueError(
            f"No character ID was found for '{account}'. Check the name."
        )

    inventory_url = (
        f"{CHARACTER_PAGE_URL}/Inventory?"
        f"{urlencode({'ccid': character_id.group(1)})}"
    )
    inventory_text = _fetch_text(inventory_url)
    if inventory_text.strip() == "error":
        raise ValueError(f"AQ did not return inventory for '{account}'.")
    inventory = json.loads(inventory_text)
    if not isinstance(inventory, list):
        raise ValueError("AQ returned an unexpected inventory format.")

    classes: list[str] = []
    seen: set[str] = set()
    for item in inventory:
        if not isinstance(item, dict):
            raise ValueError("AQ returned an invalid inventory entry.")
        if item.get("strType") != "Class":
            continue

        name = item.get("strName")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("AQ returned a class without a name.")
        name = re.sub(r"\s*\(Rank\s+\d+\)\s*$", "", name.strip(), flags=re.I)
        if name not in seen:
            classes.append(name)
            seen.add(name)
    return classes
