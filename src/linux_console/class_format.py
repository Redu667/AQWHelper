from dataclasses import dataclass
from typing import Any

# Skill/passive info is plain text or a list of {"text": ..., "color": ...}
# segments (see DESCRIPTION_COLORS in class_data.py).
Info = str | tuple[dict[str, str], ...]


@dataclass(frozen=True)
class Skill:
    name: str = ""
    info: Info = ""


@dataclass(frozen=True)
class Slot:
    """One gear slot: the best enhancement, an alternative, and a fallback."""

    best: str = ""
    alternative: str = ""
    base: str = "Type"


@dataclass(frozen=True)
class Mode:
    """Enhancements for one play mode (Base, Solo, Group or Special)."""

    cls: Slot = Slot()
    helm: Slot = Slot()
    weapon: Slot = Slot()
    cape: Slot = Slot()
    tonic: str = ""
    elixir: str = ""
    potion: str = ""


@dataclass(frozen=True)
class ClassDef:
    """A class entry.

    Fields left as None are empty, or inherited from `same_as` when set.
    Fields given explicitly override the inherited ones.
    """

    name: str
    description: Info | None = None
    model: str | None = None
    skills: tuple[Skill, ...] | None = None
    passives: tuple[Skill, ...] | None = None
    base: Mode | None = None
    solo: Mode | None = None
    group: Mode | None = None
    special: Mode | None = None
    same_as: str | None = None

    def field_values(self) -> dict[str, Any]:
        return {
            "model": self.model,
            "description": self.description,
            "skills": self.skills,
            "passives": self.passives,
            "base": self.base,
            "solo": self.solo,
            "group": self.group,
            "special": self.special,
        }
