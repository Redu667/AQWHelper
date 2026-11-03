import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any


ENHANCEMENT_MODES = ("Solo", "Group", "Ultra")
ENHANCEMENT_SLOTS = ("Class", "Helm", "Weapon", "Cape")


def class_data_directory() -> Path:
    data_home = Path(
        os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share"
    )
    return data_home / "aqw-helper" / "classes"


def class_data_path(class_name: str, directory: Path | None = None) -> Path:
    normalized_name = class_name.strip()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized_name.casefold()).strip("-")
    slug = slug[:80] or "class"
    digest = hashlib.sha256(normalized_name.casefold().encode("utf-8")).hexdigest()[:8]
    return (directory or class_data_directory()) / f"{slug}-{digest}.json"


def class_data_names(directory: Path | None = None) -> list[str]:
    data_directory = directory or class_data_directory()
    names: list[str] = []
    seen: set[str] = set()
    for path in data_directory.glob("*.json"):
        try:
            data: Any = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        name = data.get("class_name")
        if not isinstance(name, str) or not name.strip():
            continue
        normalized = name.strip()
        folded = normalized.casefold()
        if folded != "template" and folded not in seen:
            names.append(normalized)
            seen.add(folded)
    return sorted(names, key=str.casefold)


def _template(class_name: str) -> dict[str, Any]:
    return {
        "class_name": class_name,
        "enhancements": {
            mode: {
                slot: {"type": "Type", "info": ""}
                for slot in ENHANCEMENT_SLOTS
            }
            for mode in ENHANCEMENT_MODES
        },
        "skills": [
            {"name": "", "info": ""}
            for number in range(1, 6)
        ],
        "passives": [
            {"name": "", "info": ""}
            for _ in range(2)
        ],
    }


def _validate_class_data(data: Any, class_name: str) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ValueError("Class data must be a JSON object.")

    enhancements = data.get("enhancements")
    skills = data.get("skills")
    passives = (
        data["passives"]
        if "passives" in data
        else _template(class_name)["passives"]
    )
    if (
        not isinstance(enhancements, dict)
        or not isinstance(skills, list)
        or not isinstance(passives, list)
    ):
        raise ValueError(
            "Class data needs 'enhancements', 'skills', and 'passives' sections."
        )

    for mode in ENHANCEMENT_MODES:
        mode_data = enhancements.get(mode)
        if not isinstance(mode_data, dict):
            raise ValueError(f"Enhancements must include a '{mode}' object.")
        for slot in ENHANCEMENT_SLOTS:
            slot_data = mode_data.get(slot)
            if not isinstance(slot_data, dict):
                raise ValueError(f"{mode}.{slot} must be an object.")
            if not isinstance(slot_data.get("type"), str):
                raise ValueError(f"{mode}.{slot}.type must be text.")
            if not isinstance(slot_data.get("info"), str):
                raise ValueError(f"{mode}.{slot}.info must be text.")

    if len(skills) != 5:
        raise ValueError("Class data must contain exactly five skills.")
    for number, skill in enumerate(skills, start=1):
        if not isinstance(skill, dict):
            raise ValueError(f"Skill {number} must be an object.")
        if not isinstance(skill.get("name"), str):
            raise ValueError(f"Skill {number}.name must be text.")
        if not isinstance(skill.get("info"), str):
            raise ValueError(f"Skill {number}.info must be text.")

    if len(passives) not in (2, 3):
        raise ValueError("Class data must contain two or three passives.")
    for number, passive in enumerate(passives, start=1):
        if not isinstance(passive, dict):
            raise ValueError(f"Passive {number} must be an object.")
        if not isinstance(passive.get("name", ""), str):
            raise ValueError(f"Passive {number}.name must be text.")
        if not isinstance(passive.get("info", ""), str):
            raise ValueError(f"Passive {number}.info must be text.")

    result = _template(class_name)
    result["enhancements"] = enhancements
    result["skills"] = [
        {
            "name": (
                ""
                if skill["name"].strip().casefold() == f"skill {number}".casefold()
                else skill["name"]
            ),
            "info": skill["info"],
        }
        for number, skill in enumerate(skills, start=1)
    ]
    result["passives"] = [
        {
            "name": passive.get("name", ""),
            "info": passive.get("info", ""),
        }
        for passive in passives
    ]
    return result


def load_or_create_class_data(
    class_name: str, directory: Path | None = None
) -> tuple[dict[str, Any], Path]:
    path = class_data_path(class_name, directory)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        data = _template(class_name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {path}: {error}") from error
    validated = _validate_class_data(data, class_name)
    if "passives" not in data:
        path.write_text(json.dumps(validated, indent=2) + "\n", encoding="utf-8")
    return validated, path
