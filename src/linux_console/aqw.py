import json
import os
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


CHARACTER_PAGE_URL = "https://account.aq.com/CharPage"
USER_AGENT = "AQW-Helper/0.1"


def config_path() -> Path:
    config_home = Path(
        os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config"
    )
    return config_home / "aqw-helper" / "config.json"


def load_default_account(path: Path) -> str | None:
    try:
        config: Any = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None

    if not isinstance(config, dict):
        raise ValueError("The saved AQW Helper settings are not a JSON object.")

    account = config.get("account")
    if account is None:
        return None
    if not isinstance(account, str) or not account.strip():
        raise ValueError("The saved account name is invalid.")
    return account.strip()


def load_account_history(path: Path) -> list[str]:
    try:
        config: Any = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []

    if not isinstance(config, dict):
        raise ValueError("The saved AQW Helper settings are not a JSON object.")

    history = config.get("account_history", [])
    if not isinstance(history, list) or any(
        not isinstance(account, str) or not account.strip() for account in history
    ):
        raise ValueError("The saved character history is invalid.")

    unique_history: list[str] = []
    seen: set[str] = set()
    for account in history:
        normalized = account.strip()
        folded = normalized.casefold()
        if folded not in seen:
            unique_history.append(normalized)
            seen.add(folded)
    return unique_history


def save_default_account(path: Path, account: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        config: Any = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        config = {}
    except json.JSONDecodeError:
        config = {}
    if not isinstance(config, dict):
        config = {}

    history = config.get("account_history", [])
    if not isinstance(history, list) or any(
        not isinstance(item, str) for item in history
    ):
        history = []
    history = [
        item
        for item in history
        if item.strip().casefold() != account.strip().casefold()
    ]
    history.append(account.strip())
    path.write_text(
        json.dumps({"account": account, "account_history": history}, indent=2) + "\n",
        encoding="utf-8",
    )


def remove_saved_account(path: Path, account: str) -> bool:
    try:
        config: Any = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return False

    if not isinstance(config, dict):
        raise ValueError("The saved AQW Helper settings are not a JSON object.")

    history = config.get("account_history", [])
    if not isinstance(history, list) or any(
        not isinstance(item, str) or not item.strip() for item in history
    ):
        raise ValueError("The saved character history is invalid.")

    normalized_name = account.strip().casefold()
    remaining = [
        item
        for item in history
        if item.strip().casefold() != normalized_name
    ]
    default_account = config.get("account")
    default_matches = (
        isinstance(default_account, str)
        and default_account.strip().casefold() == normalized_name
    )
    removed = len(remaining) != len(history) or default_matches
    if not removed:
        return False

    config["account_history"] = remaining
    if default_matches:
        config.pop("account", None)
    path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
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
