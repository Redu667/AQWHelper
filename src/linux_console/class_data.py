import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

from linux_console.aqw import (
    AVAILABLE_ENHANCEMENTS,
    DEFAULT_ENHANCEMENTS,
    ENHANCEMENT_ADDONS,
)


ENHANCEMENT_MODES = ("Base", "Solo", "Group", "Special")
ENHANCEMENT_SLOTS = ("Class", "Helm", "Weapon", "Cape")
ENHANCEMENT_OPTIONS = ("best", "alternative")
POTION_TYPES = ("Tonic", "Elixir", "Potion")
ENHANCEMENT_DATA_SECTIONS = ("enhancements", "defaults", "addons")


def class_data_directory() -> Path:
    data_home = Path(
        os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share"
    )
    return data_home / "aqw-helper" / "classes"


def class_template_directory() -> Path:
    return Path(__file__).parent / "class_templates"


def enhancement_data_path(data_directory: Path | None = None) -> Path:
    directory = data_directory or class_data_directory().parent
    return directory / "enhancements.json"


def class_data_path(class_name: str, directory: Path | None = None) -> Path:
    normalized_name = class_name.strip()
    slug = re.sub(r"[^A-Za-z0-9]+", "_", normalized_name).strip("_")
    slug = slug[:80] or "class"
    return (directory or class_data_directory()) / f"{slug}.json"


def _legacy_class_data_paths(
    class_name: str,
    directory: Path,
) -> tuple[Path, ...]:
    normalized_name = class_name.strip()
    digest = hashlib.sha256(normalized_name.casefold().encode("utf-8")).hexdigest()[:8]
    kebab_slug = re.sub(r"[^a-z0-9]+", "-", normalized_name.casefold()).strip("-")
    underscored_slug = re.sub(r"[^A-Za-z0-9]+", "_", normalized_name).strip("_")
    return (
        directory / f"{(kebab_slug[:80] or 'class')}-{digest}.json",
        directory / f"{(underscored_slug[:80] or 'class')}_{digest}.json",
    )


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
                **{
                    slot: {
                        "best": {"type": ""},
                        "alternative": {
                            "type": "",
                            "base": {"type": "Type"},
                        },
                    }
                    for slot in ENHANCEMENT_SLOTS
                },
                "Potions": {potion: "" for potion in POTION_TYPES},
            }
            for mode in ENHANCEMENT_MODES
        },
        "skills": [
            {"name": "", "info": ""} for _ in range(5)
        ],
        "passives": [
            {"name": "", "info": ""}
            for _ in range(2)
        ],
    }


def _merge_class_defaults(defaults: Any, overrides: Any) -> Any:
    if isinstance(defaults, dict) and isinstance(overrides, dict):
        return {
            key: _merge_class_defaults(defaults.get(key), overrides.get(key))
            for key in defaults.keys() | overrides.keys()
        }
    if isinstance(defaults, list) and isinstance(overrides, list):
        return [
            _merge_class_defaults(
                defaults[index] if index < len(defaults) else None,
                overrides[index] if index < len(overrides) else None,
            )
            for index in range(max(len(defaults), len(overrides)))
        ]
    if isinstance(defaults, str) and isinstance(overrides, str):
        return defaults if not overrides.strip() or overrides.strip() == "Type" else overrides
    return overrides if overrides is not None else defaults


def _enhancement_data_template() -> dict[str, Any]:
    return {
        "enhancements": {
            name: {"info": ""}
            for name in AVAILABLE_ENHANCEMENTS
            if name not in ENHANCEMENT_ADDONS
        },
        "defaults": {name: {"info": ""} for name in DEFAULT_ENHANCEMENTS},
        "addons": {name: {"info": ""} for name in ENHANCEMENT_ADDONS},
    }


def _validate_enhancement_data(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ValueError("Enhancement data must be a JSON object.")

    template = _enhancement_data_template()
    result: dict[str, Any] = {}
    for section in ENHANCEMENT_DATA_SECTIONS:
        section_data = data.get(section)
        if not isinstance(section_data, dict):
            raise ValueError(f"Enhancement data must include a '{section}' object.")
        expected_names = template[section]
        if set(section_data) != set(expected_names):
            raise ValueError(
                f"Enhancement data '{section}' must contain exactly the "
                "supported names."
            )
        result[section] = {}
        for name in expected_names:
            entry = section_data[name]
            if not isinstance(entry, dict) or not isinstance(
                entry.get("info"), str
            ):
                raise ValueError(f"{section}.{name}.info must be text.")
            result[section][name] = {"info": entry["info"]}
    return result


def load_or_create_enhancement_data(
    path: Path | None = None,
) -> tuple[dict[str, Any], Path]:
    data_path = path or enhancement_data_path()
    try:
        data: Any = json.loads(data_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        data = _enhancement_data_template()
        data_path.parent.mkdir(parents=True, exist_ok=True)
        data_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {data_path}: {error}") from error
    return _validate_enhancement_data(data), data_path


def save_enhancement_data(path: Path, data: dict[str, Any]) -> None:
    validated = _validate_enhancement_data(data)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(validated, indent=2) + "\n", encoding="utf-8")


def enhancement_info(data: dict[str, Any], name: str) -> str:
    for base in DEFAULT_ENHANCEMENTS:
        prefix = f"{base} "
        if name.startswith(prefix):
            addon = name.removeprefix(prefix)
            if addon in ENHANCEMENT_ADDONS:
                return data["addons"][addon]["info"]
    if name in DEFAULT_ENHANCEMENTS:
        return data["defaults"][name]["info"]
    return data["enhancements"].get(name, {}).get("info", "")


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

    mode_sources = {
        "Base": ("Base", "Solo"),
        "Solo": ("Solo",),
        "Group": ("Group",),
        "Special": ("Special", "Ultra"),
    }
    normalized_modes: dict[str, dict[str, Any]] = {}
    for mode, source_names in mode_sources.items():
        mode_data = next(
            (
                enhancements[source]
                for source in source_names
                if isinstance(enhancements.get(source), dict)
            ),
            None,
        )
        if not isinstance(mode_data, dict):
            raise ValueError(f"Enhancements must include a '{mode}' object.")
        normalized_modes[mode] = {}
        for slot in ENHANCEMENT_SLOTS:
            slot_data = mode_data.get(slot)
            if not isinstance(slot_data, dict):
                raise ValueError(f"{mode}.{slot} must be an object.")
            if "type" in slot_data or "info" in slot_data:
                options = {
                    "best": {"type": ""},
                    "alternative": {
                        "type": slot_data.get("type", ""),
                        "base": {"type": "Type"},
                    },
                }
            else:
                best = slot_data.get("best", {"type": ""})
                if "alternative" in slot_data:
                    raw_alternative = slot_data["alternative"]
                else:
                    raw_alternative = slot_data.get(
                        "backup",
                        slot_data.get("default", {"type": ""}),
                    )
                if isinstance(raw_alternative, dict):
                    alternative = {"type": raw_alternative.get("type", "")}
                    base = raw_alternative.get("base")
                    if not isinstance(base, dict):
                        old_default = slot_data.get("default")
                        base = {
                            "type": (
                                old_default.get("type", "Type")
                                if isinstance(old_default, dict)
                                else "Type"
                            )
                        }
                    alternative["base"] = base
                else:
                    alternative = raw_alternative
                options = {"best": best, "alternative": alternative}
            for option in ENHANCEMENT_OPTIONS:
                candidate = options[option]
                if not isinstance(candidate, dict):
                    raise ValueError(f"{mode}.{slot}.{option} must be an object.")
                name = candidate.get("type")
                if not isinstance(name, str):
                    raise ValueError(f"{mode}.{slot}.{option}.type must be text.")
                if name.strip() not in _available_class_enhancements():
                    raise ValueError(
                        f"{mode}.{slot}.{option}.type is not an available enhancement."
                    )
            alternative = options["alternative"]
            base = alternative.get("base")
            if not isinstance(base, dict) or not isinstance(base.get("type"), str):
                raise ValueError(f"{mode}.{slot}.alternative.base.type must be text.")
            if base["type"].strip() not in _available_class_enhancements():
                raise ValueError(
                    f"{mode}.{slot}.alternative.base.type is not an available "
                    "enhancement."
                )
            normalized_modes[mode][slot] = {
                "best": {"type": options["best"]["type"]},
                "alternative": {
                    "type": alternative["type"],
                    "base": {"type": base["type"]},
                },
            }
        potions = mode_data.get(
            "Potions",
            {potion: "" for potion in POTION_TYPES},
        )
        if isinstance(potions, list):
            if len(potions) != len(POTION_TYPES):
                raise ValueError(
                    f"{mode}.Potions must contain exactly three lines."
                )
            potions = {
                potion: potions[index]
                for index, potion in enumerate(POTION_TYPES)
            }
        if (
            not isinstance(potions, dict)
            or set(potions) != set(POTION_TYPES)
            or any(not isinstance(potions[potion], str) for potion in POTION_TYPES)
        ):
            raise ValueError(
                f"{mode}.Potions must contain Tonic, Elixir, and Potion text."
            )
        normalized_modes[mode]["Potions"] = {
            potion: potions[potion] for potion in POTION_TYPES
        }

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
    result["enhancements"] = normalized_modes
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


def _import_legacy_enhancement_info(
    data: Any,
    shared_data: dict[str, Any],
) -> bool:
    if not isinstance(data, dict):
        return False
    enhancements = data.get("enhancements")
    if not isinstance(enhancements, dict):
        return False

    changed = False
    for mode_data in enhancements.values():
        if not isinstance(mode_data, dict):
            continue
        for slot in ENHANCEMENT_SLOTS:
            slot_data = mode_data.get(slot)
            if not isinstance(slot_data, dict):
                continue
            options = ("default",) if "type" in slot_data or "info" in slot_data else (
                "best",
                "backup",
                "default",
                "alternative",
            )
            for option in options:
                candidate = slot_data if options == ("default",) else slot_data.get(option)
                if not isinstance(candidate, dict):
                    continue
                info = candidate.get("info")
                name = candidate.get("type")
                if not isinstance(info, str) or not info.strip() or not isinstance(
                    name, str
                ):
                    continue
                target = _enhancement_data_entry(shared_data, name.strip())
                if target is not None and not target["info"].strip():
                    target["info"] = info
                    changed = True
    return changed


def _enhancement_data_entry(
    data: dict[str, Any],
    name: str,
) -> dict[str, str] | None:
    for base in DEFAULT_ENHANCEMENTS:
        prefix = f"{base} "
        if name.startswith(prefix):
            addon = name.removeprefix(prefix)
            if addon in ENHANCEMENT_ADDONS:
                return data["addons"][addon]
    if name in DEFAULT_ENHANCEMENTS:
        return data["defaults"][name]
    return data["enhancements"].get(name)


def load_or_create_class_data(
    class_name: str,
    directory: Path | None = None,
    shared_enhancement_data: dict[str, Any] | None = None,
    shared_enhancement_path: Path | None = None,
) -> tuple[dict[str, Any], Path]:
    path = class_data_path(class_name, directory)
    legacy_path: Path | None = None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        for candidate in _legacy_class_data_paths(class_name, path.parent):
            if candidate.is_file():
                legacy_path = candidate
                break
        if legacy_path is None:
            data = _template(class_name)
        else:
            try:
                data = json.loads(legacy_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON in {legacy_path}: {error}"
                ) from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {path}: {error}") from error
    stored_name = data.get("class_name") if isinstance(data, dict) else None
    if (
        isinstance(stored_name, str)
        and stored_name.strip().casefold() != class_name.strip().casefold()
    ):
        raise ValueError(
            f"Class data file {path} belongs to {stored_name!r}, "
            f"not {class_name!r}."
        )
    if shared_enhancement_data is not None and _import_legacy_enhancement_info(
        data,
        shared_enhancement_data,
    ):
        if shared_enhancement_path is not None:
            save_enhancement_data(
                shared_enhancement_path,
                shared_enhancement_data,
            )
    validated = _validate_class_data(data, class_name)
    if (
        legacy_path is not None
        or not path.exists()
        or "passives" not in data
        or data.get("enhancements") != validated["enhancements"]
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(validated, indent=2) + "\n", encoding="utf-8")
    if legacy_path is not None:
        legacy_path.unlink()
    template_path = class_data_path(class_name, class_template_directory())
    try:
        template_data: Any = json.loads(template_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        template_data = _template(class_name)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in class template {template_path}: {error}"
        ) from error
    validated_template = _validate_class_data(template_data, class_name)
    return _validate_class_data(
        _merge_class_defaults(validated_template, validated),
        class_name,
    ), path
