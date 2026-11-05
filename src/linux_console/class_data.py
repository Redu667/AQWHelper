from pathlib import Path
from typing import Any

from linux_console.aqw import (
    AVAILABLE_ENHANCEMENTS,
    DEFAULT_ENHANCEMENTS,
    ENHANCEMENT_ADDONS,
)
from linux_console.class_schema import ClassDef, Mode, Skill, Slot
from linux_console.classes import CLASSES
from linux_console.enhancement_info import (
    ADDON_INFO,
    DEFAULT_INFO,
    ENHANCEMENT_INFO,
)


ENHANCEMENT_MODES = ("Base", "Solo", "Group", "Special")
ENHANCEMENT_SLOTS = ("Class", "Helm", "Weapon", "Cape")
ENHANCEMENT_OPTIONS = ("best", "alternative")
POTION_TYPES = ("Tonic", "Elixir", "Potion")
DESCRIPTION_COLORS = frozenset(
    {"red", "green", "yellow", "blue", "magenta", "cyan", "white"}
)


def _validate_description(value: Any, field: str) -> list[dict[str, str]]:
    if isinstance(value, str):
        return [{"text": value}] if value else []
    if not isinstance(value, list):
        raise ValueError(f"{field} must be text or a list of text/color objects.")

    segments: list[dict[str, str]] = []
    for index, segment in enumerate(value):
        segment_field = f"{field}[{index}]"
        if (
            not isinstance(segment, dict)
            or set(segment) - {"text", "color"}
            or not isinstance(segment.get("text"), str)
        ):
            raise ValueError(
                f"{segment_field} must contain text and an optional color."
            )
        text = segment["text"]
        color = segment.get("color")
        if "color" in segment and (
            not isinstance(color, str) or color not in DESCRIPTION_COLORS
        ):
            raise ValueError(
                f"{segment_field}.color must be one of "
                f"{', '.join(sorted(DESCRIPTION_COLORS))}."
            )
        if text:
            segments.append(
                {
                    "text": text,
                    **({"color": color} if "color" in segment else {}),
                }
            )
    return segments


def enhancement_info(name: str) -> list[dict[str, str]]:
    if name in ENHANCEMENT_ADDONS:
        info = ADDON_INFO.get(name, "")
    elif name in DEFAULT_ENHANCEMENTS:
        info = DEFAULT_INFO.get(name, "")
    else:
        info = ENHANCEMENT_INFO.get(name, "")
        for base in DEFAULT_ENHANCEMENTS:
            addon = name.removeprefix(f"{base} ")
            if name.startswith(f"{base} ") and addon in ENHANCEMENT_ADDONS:
                info = ADDON_INFO.get(addon, "")
    return _validate_description(info, f"{name}.info")


def resolve_enhancements(
    candidates: dict[str, Any],
    owned_enhancements: set[str],
) -> list[tuple[str, dict[str, str]]]:
    owned = (
        owned_enhancements
        | set(DEFAULT_ENHANCEMENTS)
        | set(ENHANCEMENT_ADDONS)
    )
    available: list[tuple[str, dict[str, str]]] = []
    for option in ENHANCEMENT_OPTIONS:
        candidate = candidates[option]
        name = candidate["type"].strip()
        if name and _is_owned(name, owned):
            available.append((option, _effective_candidate(candidate, owned)))
    if available:
        return available
    base = candidates["alternative"]["base"]
    return [("base", _effective_candidate(base, owned))]


def _available_class_enhancements() -> set[str]:
    names = {"", "Type", *AVAILABLE_ENHANCEMENTS, *DEFAULT_ENHANCEMENTS}
    names.update(
        f"{base} {addon}"
        for base in DEFAULT_ENHANCEMENTS
        for addon in ENHANCEMENT_ADDONS
    )
    return names


def _addon_from_default(name: str) -> str | None:
    for base in DEFAULT_ENHANCEMENTS:
        prefix = f"{base} "
        if name.startswith(prefix):
            addon = name.removeprefix(prefix)
            return addon if addon in ENHANCEMENT_ADDONS else None
    return None


def _is_owned(name: str, owned: set[str]) -> bool:
    addon = _addon_from_default(name)
    if addon is not None:
        return addon in owned
    return name in owned


def _effective_candidate(
    candidate: dict[str, str],
    owned: set[str],
) -> dict[str, str]:
    name = candidate["type"].strip()
    addon = _addon_from_default(name)
    if addon is None or addon in owned:
        return candidate

    base = name.removesuffix(f" {addon}")
    return {**candidate, "type": base}


CLASS_DEFINITIONS_FILE = Path(__file__).with_name("classes.py")
SKILL_COUNT = 5
MIN_PASSIVES = 2
MAX_PASSIVES = 3
MODE_FIELDS = {"Base": "base", "Solo": "solo", "Group": "group", "Special": "special"}
SLOT_FIELDS = {"Class": "cls", "Helm": "helm", "Weapon": "weapon", "Cape": "cape"}
POTION_FIELDS = {"Tonic": "tonic", "Elixir": "elixir", "Potion": "potion"}


def class_data_names() -> list[str]:
    return sorted((definition.name for definition in CLASSES), key=str.casefold)


def _find_class(class_name: str) -> ClassDef:
    folded = class_name.strip().casefold()
    for definition in CLASSES:
        if definition.name.casefold() == folded:
            return definition
    raise ValueError(f"Unknown class: {class_name}")


def _resolved_fields(definition: ClassDef) -> dict[str, Any]:
    chain: list[ClassDef] = []
    current: ClassDef | None = definition
    while current is not None:
        if current in chain:
            names = " -> ".join(item.name for item in (*chain, current))
            raise ValueError(f"Class same_as cycle: {names}")
        chain.append(current)
        current = _find_class(current.same_as) if current.same_as else None

    fields: dict[str, Any] = {}
    for item in reversed(chain):
        fields.update(
            {key: value for key, value in item.field_values().items() if value is not None}
        )
    return fields


def _check_enhancement(name: str, field: str) -> str:
    if name.strip() not in _available_class_enhancements():
        raise ValueError(f"{field} is not an available enhancement: {name!r}")
    return name


def _slot_data(slot: Slot, field: str) -> dict[str, Any]:
    return {
        "best": {"type": _check_enhancement(slot.best, f"{field}.best")},
        "alternative": {
            "type": _check_enhancement(slot.alternative, f"{field}.alternative"),
            "base": {"type": _check_enhancement(slot.base, f"{field}.base")},
        },
    }


def _mode_data(mode: Mode, field: str) -> dict[str, Any]:
    data: dict[str, Any] = {
        slot: _slot_data(getattr(mode, attribute), f"{field}.{slot}")
        for slot, attribute in SLOT_FIELDS.items()
    }
    data["Potions"] = {
        potion: getattr(mode, attribute)
        for potion, attribute in POTION_FIELDS.items()
    }
    return data


def _skill_data(skill: Skill, field: str) -> dict[str, Any]:
    info = list(skill.info) if isinstance(skill.info, tuple) else skill.info
    return {"name": skill.name, "info": _validate_description(info, f"{field}.info")}


def load_class_data(class_name: str) -> dict[str, Any]:
    definition = _find_class(class_name)
    fields = _resolved_fields(definition)
    name = definition.name

    skills = tuple(fields.get("skills", ()))
    if len(skills) > SKILL_COUNT:
        raise ValueError(f"{name} has more than {SKILL_COUNT} skills.")
    skills += (Skill(),) * (SKILL_COUNT - len(skills))

    passives = tuple(fields.get("passives", ()))
    if len(passives) > MAX_PASSIVES:
        raise ValueError(f"{name} has more than {MAX_PASSIVES} passives.")
    passives += (Skill(),) * (MIN_PASSIVES - len(passives))

    description = fields.get("description", "")
    if isinstance(description, tuple):
        description = list(description)

    return {
        "class_name": name,
        "model": fields.get("model", ""),
        "description": _validate_description(description, f"{name}.description"),
        "enhancements": {
            mode: _mode_data(fields.get(attribute) or Mode(), f"{name}.{mode}")
            for mode, attribute in MODE_FIELDS.items()
        },
        "skills": [
            _skill_data(skill, f"{name}.skill {number}")
            for number, skill in enumerate(skills, start=1)
        ],
        "passives": [
            _skill_data(passive, f"{name}.passive {number}")
            for number, passive in enumerate(passives, start=1)
        ],
    }
