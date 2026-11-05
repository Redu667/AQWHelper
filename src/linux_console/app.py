from __future__ import annotations

import argparse
import asyncio
import logging
import os
import re
from pathlib import Path
import sys
from typing import Any

from rich.cells import cell_len
from rich.text import Text
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.content import Content
from textual.events import Click, Key, Resize
from textual.message import Message
from textual.suggester import Suggester
from textual.widgets import Button, Input, ListItem, ListView, Static

from linux_console.aqw import (
    AVAILABLE_ENHANCEMENTS,
    DEFAULT_ENHANCEMENTS,
    ENHANCEMENT_ADDONS,
    TOGGLEABLE_ENHANCEMENTS,
    config_path,
    fetch_classes,
    load_character_enhancements,
    load_profiles,
    remove_profile,
    save_character_enhancements,
    save_profile,
)
from linux_console.class_data import (
    ENHANCEMENT_MODES,
    ENHANCEMENT_SLOTS,
    CLASS_DEFINITIONS_FILE,
    class_data_names,
    enhancement_info,
    load_class_data,
    resolve_enhancements,
)
from linux_console.version_check import current_version, update_available
from linux_console.release_update import (
    NoPublishedReleaseError,
    install_latest_release,
)

logger = logging.getLogger(__name__)
COMMANDS = (
    (" char", "Load and save a character account"),
    (" reload", "Reload the character's classes"),
    (" class", "Display any class, owned or not"),
    (" enhancements", "Display all enhancements"),
    (" stats", "Display stats details"),
    (" return", "Return to the Commands home page"),
    (" navi", "Enter navigation mode"),
    (" update", "Update the app"),
    (" quit", "Close the app"),
    (" advanced", "Display keyboard shortcuts"),
)
COMMAND_ALIASES = {
    "c": "char",
    "ch": "char",
    "character": "char",
    "q": "quit",
    "r": "return",
    "n": "navi",
    "rl": "reload",
    "up": "update",
    "cl": "class",
    "classes": "class",
    "enh": "enhancements",
    "st": "stats",
    "adv": "advanced",
}
ENHANCEMENT_COLORS = {
    "Vim": "#86efac",
    "Examen": "#fde68a",
    "Anima": "#fca5a5",
    "Pneuma": "#93c5fd",
    "Hearty": "#ff69b4",
    "Acheron": "#ffffff",
    "Elysium": "#60a5fa",
    "Dauntless": "#f87171",
    "Fighter": "#8b0000",
    "Thief": "#006400",
    "Wizard": "#464688",
    "Healer": "#ffffff",
    "Spellbreaker": "#cd7f32",
    "Hybrid": "#d2b48c",
    "Lucky": "#e9a8f4",
    "Awe Blast": "#aec2f9",
    "Spiral Carve": "#c9f9ae",
    "Health Vamp": "#f9aeae",
    "Mana Vamp": "#aeecf9",
    "Powerword DIE": "#dfaef9",
}
DEFAULT_ENHANCEMENT_COLOR = "#f7b176"
NAV_ACTIONS = (
    "nav_up",
    "nav_down",
    "nav_select",
    "nav_right",
    "nav_back",
    "nav_left",
    "nav_toggle_pane",
)
ENHANCEMENT_GROUPS = (
    ("Base", DEFAULT_ENHANCEMENTS),
    ("Weapon - [#aeecf9]Awe[#ffffff]", ENHANCEMENT_ADDONS),
    ("Weapon - [#f7b176]Forge[#ffffff]", ("Lacerate", "Smite", "Praxis", "Acheron", "Hero's Valiance", "Elysium", "Arcana's Concerto", "Dauntless", "Ravenous",)),
    ("Helm - [#f7b176]Forge[#ffffff]", ("Forge", "Vim", "Examen", "Anima", "Pneuma", "Hearty")),
    ("Cape - [#f7b176]Forge[#ffffff]", ("Absolution", "Vainglory", "Avarice", "Lament", "Penitence")),
)
CLASS_MODELS = (
    "Power Melee",
    "Dodge Melee",
    "Tank Melee",
    "Power Caster",
    "Offensive Caster",
    "Defensive Caster",
    "Full Hybrid",
    "Luck Hybrid",
)
CLASS_MODEL_COLORS = {
    "Power Melee": "#ca7a34",
    "Dodge Melee": "#78a849",
    "Tank Melee": "#af4040",
    "Power Caster": "#76e4f7",
    "Offensive Caster": "#7694f7",
    "Defensive Caster": "#8776f7",
    "Full Hybrid": "#ffa053",
    "Luck Hybrid": "#ffea7e",
}
CLASS_MODEL_DESCRIPTIONS = {
    "Power Melee": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★★[/b #eac43c]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        "\nCrit Chance [#5eff00]↑↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\nDodge [#5eff00]↑↑[#ffffff]"
        "\nHaste [#5eff00]↑↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★☆☆[/b #eac43c]"
        "\nSpell Power [#5eff00]↑↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#5eff00]↑↑[#ffffff]"
        "\nCritical Chance [#78a849]↑[#ffffff]"
        "\nAttack Power [#78a849]↑[#ffffff]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
    "Dodge Melee": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        "\nCrit Chance [#78a849]↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\nDodge [#5eff00]↑↑[#ffffff]"
        "\nHaste [#5eff00]↑↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★☆☆[/b #eac43c]"
        "\nSpell Power [#5eff00]↑↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#5eff00]↑↑[#ffffff]"
        "\nCritical Chance [#78a849]↑[#ffffff]"
        "\nAttack Power [#78a849]↑[#ffffff]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
    "Tank Melee": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        "\nCrit Chance [#78a849]↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★☆☆[/b #eac43c]"
        "\nSpell Power [#5eff00]↑↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#5eff00]↑↑[#ffffff]"
        "\nCritical Chance [#78a849]↑[#ffffff]"
        "\nAttack Power [#78a849]↑[#ffffff]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
    "Power Caster": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★☆☆[/b #eac43c]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★★[/b #eac43c]"
        "\nSpell Power [#5eff00]↑↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nMagical Boost [#78a849]↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★★☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nCrit Chance [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#5eff00]↑↑[#ffffff]"
        "\nCritical Chance [#78a849]↑[#ffffff]"
        "\nSpell Power [#78a849]↑[#ffffff]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
    "Offensive Caster": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★☆☆[/b #eac43c]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★★[/b #eac43c]"
        "\nSpell Power [#5eff00]↑↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nMagical Boost [#78a849]↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★★☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nCrit Chance [#5eff00]↑↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#5eff00]↑↑[#ffffff]"
        "\nCritical Chance [#78a849]↑[#ffffff]"
        "\nSpell Power [#78a849]↑[#ffffff]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
    "Defensive Caster": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★☆☆[/b #eac43c]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★★[/b #eac43c]"
        "\nSpell Power [#78a849]↑↑[#ffffff]"
        "\nHaste [#5eff00]↑↑[#ffffff]"
        "\nMagical Boost [#78a849]↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★★☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nCrit Chance [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#5eff00]↑↑[#ffffff]"
        "\nCritical Chance [#78a849]↑[#ffffff]"
        "\nSpell Power [#78a849]↑[#ffffff]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
    "Full Hybrid": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        "\nCrit Chance [#78a849]↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\nDodge [#5eff00]↑↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★☆[/b #eac43c]"
        "\nSpell Power [#5eff00]↑↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nMagical Boost [#78a849]↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#5eff00]↑↑[#ffffff]"
        "\nCritical Chance [#78a849]↑[#ffffff]"
        "\nAttack Power [#78a849]↑[#ffffff]"
        "\nSpell Power [#78a849]↑[#ffffff]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
    "Luck Hybrid": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\nAttack Power [#78a849]↑[#ffffff]"
        "\nCrit Chance [#78a849]↑[#ffffff]"
        
        "\n\n[b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\nHealth [#78a849]↑[#ffffff]"

        "\n\n[b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★☆[/b #eac43c]"
        "\nSpell Power [#78a849]↑[#ffffff]"
        "\nHaste [#78a849]↑[#ffffff]"
        "\nMagical Boost [#78a849]↑[#ffffff]"
        "\nMagical Resistance [#78a849]↑[#ffffff]"

        "\n\n[b #fde68a]WIS[/b #fde68a] [b #eac43c]★★★[/b #eac43c]"
        "\nDodge [#78a849]↑[#ffffff]"
        "\nCrit Chance [#78a849]↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"

        "\n\n[b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\nCritical Damage [#78a849]↑[#ffffff]"
        "\nCritical Chance [#5eff00]↑↑[#ffffff]"
        "\nAttack Power [#5eff00]↑↑[#ffffff]"
        "\nSpell Power [#5eff00]↑↑[#ffffff]"
        "\nDodge [#5eff00]↑↑[#ffffff]"
        "\nHaste [#5eff00]↑↑[#ffffff]"
        "\nHit Chance [#78a849]↑[#ffffff]"
    ),
}


def enhancement_color(name: str) -> str:
    color = ENHANCEMENT_COLORS.get(name)
    if color is not None:
        return color
    for root in DEFAULT_ENHANCEMENTS:
        if name.startswith(f"{root} "):
            return ENHANCEMENT_COLORS[root]
    return DEFAULT_ENHANCEMENT_COLOR


def style_description(description: str | list[dict[str, str]]) -> Text:
    if isinstance(description, str):
        return Text(description)

    styled = Text()
    for segment in description:
        styled.append(segment["text"], style=segment.get("color"))
    return styled


class NavButton(Button):
    """Left-panel button that shows a ">" marker when hovered or under the cursor."""

    class Mounted(Message):
        pass

    def on_mount(self) -> None:
        self.post_message(self.Mounted())

    def watch_mouse_hover(self, hovered: bool) -> None:
        self.refresh()

    def render(self) -> Content:
        marker = ">" if self.mouse_hover or self.has_class("nav-cursor") else " "
        return Content(f"{marker} ") + self.label


class CommandSuggester(Suggester):
    def __init__(self, app: LinuxConsoleApp) -> None:
        super().__init__(use_cache=False, case_sensitive=True)
        self.app = app

    async def get_suggestion(self, value: str) -> str | None:
        return self.app._suggest_completion(value)


class LinuxConsoleApp(App[None]):
    TITLE = "AQW Helper"
    CSS = """
    Screen {
        padding: 1;
        background: #000000;
        color: #d1d5db;
    }

    #main-ui {
        height: 1fr;
    }

    #entry-area {
        height: 3;
        dock: bottom;
    }

    #entry-area.first-run {
        height: 1fr;
        dock: none;
        align-horizontal: center;
        align-vertical: middle;
    }

    #entry-area.first-run #command-input {
        width: 48;
        border: round #4ade80;
        color: #4ade80;
    }

    #header {
        height: 7;
    }

    #banner {
        width: 1fr;
        height: 7;
        content-align: left top;
        color: #f4a261;
    }

    #version-label {
        width: auto;
        height: 1;
        margin-right: 1;
        color: #f4a261;
        text-align: right;
        content-align: right top;
    }

    #panels {
        height: 1fr;
    }

    #info-panel {
        width: 1fr;
        height: 1fr;
        padding: 0 0 1 0;
        background: #050705;
        border: round #4ade80;
        border-title-align: left;
        border-title-color: #4ade80;
        border-title-background: #050705;
    }

    #info-content {
        height: 1fr;
        margin-top: 0;
        padding: 0;
        align-horizontal: left;
    }

    #update-available {
        display: none;
        width: auto;
        min-width: 0;
        height: 1;
        margin: 0 0 0 1;
        padding: 0;
        color: #4ade80;
        background: transparent;
        border: none;
    }

    .info-action {
        width: 1fr;
        height: 1;
        margin-bottom: 1;
        padding: 0;
        color: #4ade80;
        background: transparent;
        border: none;
        text-align: left;
        content-align: left middle;
    }

    .class-description {
        padding-bottom: 0;
    }

    .info-action:hover,
    .info-action:focus,
    .info-action.-active,
    .update-choice:hover,
    .update-choice:focus,
    .update-choice.-active,
    .enhancement-toggle:hover,
    .enhancement-toggle:focus,
    .enhancement-toggle.-active {
        background: transparent;
        background-tint: transparent;
        text-style: bold;
    }

    .info-action:hover,
    .info-action.nav-cursor,
    .update-choice:hover,
    .update-choice.nav-cursor {
        color: #FFE3B5;
    }

    .enhancement-group {
        width: 1fr;
        height: auto;
        padding-left: 2;
    }

    .info-detail {
        width: 1fr;
        padding: 0 0 1 0;
        color: #d1d5db;
        text-align: left;
        content-align: left top;
    }

    .enhancement-info-detail {
        padding-left: 8;
    }

    .enhancement-category {
        height: 1;
        color: #9ca3af;
        text-style: bold;
    }

    .enhancement-spacer {
        height: 1;
    }

    .update-warning {
        width: 1fr;
        color: #f87171;
        text-align: left;
        content-align: left top;
    }

    .update-choice {
        width: auto;
        min-width: 0;
        height: 1;
        margin-right: 2;
        padding: 0;
        color: #f87171;
        background: transparent;
        border: none;
    }

    #class-list {
        height: 1fr;
        background: #050608;
        border: none;
    }

    #class-list > ListItem.-hovered,
    #class-list > ListItem.-highlight,
    #class-list > ListItem.selected {
        background: transparent;
    }

    .class-row {
        width: 1fr;
        height: 1;
    }

    .class-marker {
        width: 2;
        color: transparent;
    }

    ListItem.-hovered .class-marker {
        color: #FFE3B5;
    }

    ListItem.-hovered .class-name {
        color: #FFE3B5;
    }

    ListItem.selected .class-name {
        color: #F2C16F;
    }

    #class-list > ListItem.selected .class-marker {
        color: transparent;
    }

    #class-list.nav-active > ListItem.-highlight .class-marker {
        color: #FFE3B5;
    }

    #class-list.nav-active > ListItem.-highlight .class-name {
        color: #FFE3B5;
    }

    #class-list.nav-active > ListItem.selected .class-marker {
        color: transparent;
    }

    #class-list.nav-active > ListItem.selected .class-name {
        color: #F2C16F;
    }

    #class-panel {
        width: 1fr;
        height: 1fr;
        background: #050608;
        border: round #38bdf8;
        border-title-align: left;
        border-title-color: #38bdf8;
        border-title-background: #050608;
        border-subtitle-align: center;
        border-subtitle-color: #38bdf8;
        border-subtitle-background: #050608;
    }

    #enhancements-list {
        display: none;
        height: 1fr;
        padding: 0 1;
    }

    .enhancement-toggle {
        width: 1fr;
        height: 1;
        padding: 0;
        color: #d1d5db;
        background: transparent;
        border: none;
        text-align: left;
        content-align: left middle;
    }

    .class-name {
        width: 1fr;
        color: #98ddfa;
    }

    #command-input {
        height: 3;
        color: #f87171;
        background: #020403;
        border: round #b91c1c;
    }
    """
    BINDINGS = [
        Binding("ctrl+c", "shortcut_char", show=False, priority=True),
        Binding("ctrl+r", "shortcut_reload", show=False, priority=True),
        Binding("ctrl+e", "shortcut_enhancements", show=False, priority=True),
        Binding("ctrl+s", "shortcut_stats", show=False, priority=True),
        Binding("ctrl+x", "shortcut_return", show=False, priority=True),
        Binding("ctrl+u", "shortcut_update", show=False, priority=True),
        Binding("ctrl+a", "shortcut_advanced", show=False, priority=True),
        Binding("ctrl+z", "navigate_back", show=False, priority=True),
        Binding("escape", "quit", show=False, priority=True),
        Binding("pageup", "scroll_info_up", show=False, priority=True),
        Binding("pagedown", "scroll_info_down", show=False, priority=True),
        Binding("ctrl+n", "toggle_navigation", show=False, priority=True),
        Binding("tab", "nav_toggle_pane", show=False, priority=True),
        Binding("up", "nav_up", show=False, priority=True),
        Binding("down", "nav_down", show=False, priority=True),
        Binding("enter", "nav_select", show=False, priority=True),
        Binding("right", "nav_right", show=False, priority=True),
        Binding("left", "nav_left", show=False, priority=True),
        Binding("backspace", "nav_back", show=False, priority=True),
        Binding("w", "nav_up", show=False, priority=True),
        Binding("s", "nav_down", show=False, priority=True),
        Binding("a", "nav_left", show=False, priority=True),
        Binding("d", "nav_right", show=False, priority=True),
        ("ctrl+q", "ignore_quit", "Ignore quit"),
    ]

    def __init__(
        self,
        *,
        settings_path: Path | None = None,
        data_directory: Path | None = None,
    ) -> None:
        super().__init__()
        self.settings_path = settings_path or config_path()
        self.account: str | None = None
        self.character_classes: list[str] = []
        self.selected_enhancements = set(TOGGLEABLE_ENHANCEMENTS)
        self.selected_class = ""
        self.selected_class_data: dict[str, Any] = {}
        self.selected_class_file = Path()
        self.info_history: list[str] = []
        self.detail_counter = 0
        self.account_history: list[str] = []
        self._completion_cycle: tuple[str, str, str, list[str], int] | None = None
        self._programmatic_completion: str | None = None
        self._character_load_generation = 0
        self._loading_character_generation: int | None = None
        self.restart_requested = False
        self.nav_mode = False
        self.nav_pane = "right"
        self._nav_button: NavButton | None = None
        self.nav_header = False
        self.nav_header_item = "classes"
        self.nav_tab = "classes"
        self.enh_index = 0
        self._info_back_enabled = False
        self._info_home_enabled = False
        self._info_back_label = "← Back"
        self._info_panel_title = "Info"

    def compose(self) -> ComposeResult:
        with Vertical(id="main-ui"):
            yield Horizontal(
                Static(
                "  █████╗  ██████╗ ██╗    ██╗    ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗\n"
                " ██╔══██╗██╔═══██╗██║    ██║    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗\n"
                " ███████║██║   ██║██║ █╗ ██║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝\n"
                " ██╔══██║██║▄▄ ██║██║███╗██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗\n"
                " ██║  ██║╚██████╔╝╚███╔███╔╝    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║\n"
                " ╚═╝  ╚═╝ ╚══▀▀═╝  ╚══╝╚══╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝\n"
                " By: Potato Lady",
                    id="banner",
                ),
                Static(f"v.{current_version()}", id="version-label"),
                id="header",
            )
            with Horizontal(id="panels"):
                with Vertical(id="info-panel"):
                    yield VerticalScroll(id="info-content")
                    yield Button(
                        "↓ Update Pending",
                        id="update-available",
                        tooltip="Type /update to install the latest release",
                    )
                with Vertical(id="class-panel"):
                    yield ListView(id="class-list")
                    yield VerticalScroll(id="enhancements-list")
        with Vertical(id="entry-area"):
            yield Input(
                placeholder="Char: ",
                id="command-input",
                suggester=CommandSuggester(self),
            )

    async def on_mount(self) -> None:
        self.class_list = self.query_one("#class-list", ListView)
        await self._populate_enhancements()
        await self._clear_runtime_cache()
        self.query_one("#command-input", Input).focus()
        self._set_info_session("Commands")
        self._set_back_enabled(False)
        self._set_home_enabled(False)
        self._show_classes_tab()
        await self._show_commands()
        self.run_worker(
            self._check_for_updates(),
            name="check-for-updates",
            group="update-check",
        )

        try:
            self.account_history, account = load_profiles(self.settings_path)
        except (OSError, ValueError) as error:
            await self._set_info(f"Could not read saved profiles: {error}", "#f87171")
            return

        if account is None:
            if not self.account_history:
                self._show_first_run()
            return
        self.run_worker(
            self._load_character(account, background_startup=True),
            name="load-startup-character",
            group="character-load",
            exclusive=True,
        )

    async def _check_for_updates(self) -> None:
        try:
            available = await asyncio.to_thread(update_available)
        except (OSError, TimeoutError, UnicodeError, ValueError) as error:
            logger.warning("Could not check for AQW Helper updates: %s", error)
            return
        self.query_one("#update-available", Button).display = available

    def action_ignore_quit(self) -> None:
        pass

    async def action_shortcut_char(self) -> None:
        await self._submit_shortcut_command("char")

    async def action_shortcut_reload(self) -> None:
        await self._submit_shortcut_command("reload")

    async def action_shortcut_enhancements(self) -> None:
        await self._submit_shortcut_command("enhancements")

    async def action_shortcut_stats(self) -> None:
        await self._submit_shortcut_command("stats")

    async def action_shortcut_return(self) -> None:
        await self._submit_shortcut_command("return")

    async def action_shortcut_update(self) -> None:
        await self._submit_shortcut_command("update")

    async def action_shortcut_advanced(self) -> None:
        await self._submit_shortcut_command("advanced")

    async def _submit_shortcut_command(self, command: str) -> None:
        command_input = self.query_one("#command-input", Input)
        command_input.value = f"/{command}"
        await command_input.action_submit()

    async def action_quit(self) -> None:
        await self._clear_runtime_cache()
        await super().action_quit()

    async def _clear_runtime_cache(self) -> None:
        self.account = None
        self._update_character_placeholder()
        self.character_classes.clear()
        self.selected_enhancements = set(TOGGLEABLE_ENHANCEMENTS)
        self._clear_selected_class_data()
        self.account_history.clear()
        self._completion_cycle = None
        self._programmatic_completion = None
        self._character_load_generation += 1
        self._loading_character_generation = None
        self._info_back_enabled = False
        self._info_home_enabled = False
        class_list = self.query_one("#class-list", ListView)
        class_list.border_title = ""
        await class_list.clear()
        self._set_info_session("Info")
        await self._populate_enhancements()
        self._show_classes_tab()

    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id != "command-input":
            return
        if event.value == self._programmatic_completion:
            self._programmatic_completion = None
            return
        self._completion_cycle = None

    def on_key(self, event: Key) -> None:
        command_input = self.query_one("#command-input", Input)
        if self.focused is not command_input:
            return

        if event.key == "tab":
            completion = self._suggest_completion(command_input.value)
            if completion is not None:
                if not completion.endswith(" "):
                    completion += " "
                self._set_command_completion(command_input, completion)
                event.prevent_default()
                event.stop()
        elif event.key in ("up", "down"):
            if not command_input.cursor_at_end:
                return
            context = self._completion_context(command_input.value)
            if context is None:
                return
            command, prefix, typed = context
            cycle = self._completion_cycle
            continuing_cycle = (
                cycle is not None
                and cycle[:2] == (command, prefix)
                and typed in (cycle[2], cycle[3][cycle[4]])
            )
            if not continuing_cycle:
                candidates = self._argument_candidates(command, typed)
                if not candidates:
                    return
                index = 0 if event.key == "up" else len(candidates) - 1
                cycle = (command, prefix, typed, candidates, index)
            else:
                direction = 1 if event.key == "up" else -1
                index = (cycle[4] + direction) % len(cycle[3])
                cycle = (*cycle[:4], index)

            self._completion_cycle = cycle
            completion = f"{prefix}{cycle[3][cycle[4]]}"
            self._set_command_completion(command_input, completion)
            event.prevent_default()
            event.stop()

    def _set_command_completion(self, command_input: Input, value: str) -> None:
        self._programmatic_completion = value
        command_input.value = value
        command_input.cursor_position = len(value)

    def _completion_context(self, value: str) -> tuple[str, str, str] | None:
        match = re.match(r"^\s*(/?\S+)(\s+)(.*)$", value)
        if match is None:
            return None
        command = match.group(1).lstrip("/").casefold()
        command = COMMAND_ALIASES.get(command, command)
        if command not in ("char", "class"):
            return None
        return command, value[: match.start(3)], match.group(3)

    def _argument_candidates(self, command: str, typed: str) -> list[str]:
        if command == "char":
            candidates = list(reversed(self.account_history))
            if not candidates:
                candidates = ["CHAR"]
        else:
            candidates = class_data_names()
        if typed:
            candidates = [
                candidate
                for candidate in candidates
                if candidate.casefold().startswith(typed.casefold())
            ]
        return candidates

    def _suggest_completion(self, value: str) -> str | None:
        if not value.strip():
            return None

        context = self._completion_context(value)
        if context is not None:
            command, prefix, typed = context
            candidates = self._argument_candidates(command, typed)
            if candidates:
                candidate = candidates[0]
                completion = f"{prefix}{candidate}"
                return completion if completion != value else None
            return None

        token = value.lstrip()
        has_leading_slash = token.startswith("/")
        command_prefix = token.lstrip("/")
        command_names = [command.strip() for command, _ in COMMANDS]
        for command in command_names:
            if command.casefold().startswith(command_prefix.casefold()):
                suggestion = f"/{command}" if has_leading_slash else command
                if command.casefold() == command_prefix.casefold():
                    return f"{suggestion} "
                return suggestion
        return None

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        submitted_value = event.value.strip()
        if (
            self._is_first_run()
            and submitted_value
            and not submitted_value.startswith("/")
        ):
            self._leave_first_run()
            await self._load_character(submitted_value)
            return

        command_line = event.value.strip().lstrip("/").strip()
        event.input.value = ""
        self._completion_cycle = None
        if not command_line:
            return
        parts = command_line.split(maxsplit=1)
        command = parts[0].casefold()
        command = COMMAND_ALIASES.get(command, command)
        argument = parts[1].strip() if len(parts) == 2 else ""
        if command == "char":
            if not argument:
                await self._show_saved_characters()
                return
            if argument.startswith("-"):
                account_name = argument[1:].strip()
                if not account_name:
                    await self._set_info(
                        "Usage: char -NAME",
                        "#f87171",
                    )
                    return
                try:
                    removed = remove_profile(
                        self.settings_path,
                        account_name,
                    )
                    self.account_history, _ = load_profiles(self.settings_path)
                except (OSError, ValueError) as error:
                    await self._set_info(
                        f"Could not remove {account_name}: {error}",
                        "#f87171",
                    )
                    return
                status = (
                    f"Removed {account_name} from saved characters."
                    if removed
                    else f"{account_name} was not in saved characters."
                )
                await self._show_saved_characters(status)
                return
            if self._is_first_run():
                self._leave_first_run()
            await self._load_character(argument)
        elif command == "reload":
            if argument:
                await self._set_info("Usage: reload", "#f87171")
            elif self.account is None:
                await self._set_info("Set a character first with char NAME.", "#f87171")
            else:
                await self._load_character(self.account)
        elif command == "class":
            if argument:
                await self._show_selected_class(argument)
        elif command == "enhancements":
            if argument:
                await self._set_info("Usage: enhancements", "#f87171")
            else:
                await self._show_enhancement_catalog()
        elif command == "stats":
            if argument:
                await self._set_info("Usage: stats", "#f87171")
            else:
                await self._show_stats()
        elif command == "advanced":
            if argument:
                await self._set_info("Usage: advanced", "#f87171")
            else:
                await self._show_advanced()
        elif command == "update":
            if argument:
                await self._set_info("Usage: update", "#f87171")
            else:
                await self._show_update_confirmation()
        elif command == "return":
            if argument:
                await self._set_info("Usage: return", "#f87171")
            else:
                await self._show_commands()
        elif command == "navi":
            if argument:
                await self._set_info("Usage: navi", "#f87171")
            else:
                self._set_nav_mode(True)
        elif command == "quit":
            if argument:
                await self._set_info("Usage: quit", "#f87171")
            else:
                await self.action_quit()

    def _is_first_run(self) -> bool:
        return self.query_one("#entry-area", Vertical).has_class("first-run")

    def _show_first_run(self) -> None:
        self.query_one("#main-ui", Vertical).display = False
        entry_area = self.query_one("#entry-area", Vertical)
        entry_area.add_class("first-run")
        command_input = self.query_one("#command-input", Input)
        command_input.placeholder = ""
        command_input.border_title = "Character name"
        command_input.value = ""
        command_input.focus()

    def _leave_first_run(self) -> None:
        self.query_one("#main-ui", Vertical).display = True
        entry_area = self.query_one("#entry-area", Vertical)
        entry_area.remove_class("first-run")
        command_input = self.query_one("#command-input", Input)
        self._update_character_placeholder()
        command_input.border_title = ""
        command_input.value = ""

    def _update_character_placeholder(self) -> None:
        account = f" {self.account}" if self.account else ""
        self.query_one("#command-input", Input).placeholder = f"Char:{account}"

    async def _load_character(
        self,
        account: str,
        *,
        background_startup: bool = False,
    ) -> None:
        self._character_load_generation += 1
        generation = self._character_load_generation
        self.account = None
        self._update_character_placeholder()
        self.character_classes = []
        class_list = self.query_one("#class-list", ListView)
        self._info_back_enabled = False
        self._info_home_enabled = False
        await class_list.clear()
        self.selected_enhancements = set(TOGGLEABLE_ENHANCEMENTS)
        await self._populate_enhancements()
        await class_list.extend(
            [ListItem(Static("Loading...", classes="class-name"))]
        )
        self._loading_character_generation = generation
        try:
            classes = await asyncio.to_thread(fetch_classes, account)
        except (OSError, TimeoutError, ValueError) as error:
            if generation != self._character_load_generation:
                await self._clear_stale_loading_indicator(generation)
                return
            await class_list.clear()
            self._loading_character_generation = None
            if background_startup:
                self.notify(f"Could not load {account}: {error}", severity="error")
            else:
                await self._set_info(f"Could not load {account}: {error}", "#f87171")
            return

        if generation != self._character_load_generation:
            await self._clear_stale_loading_indicator(generation)
            return
        try:
            selected_enhancements = load_character_enhancements(
                self.settings_path,
                account,
            )
        except (OSError, ValueError) as error:
            await class_list.clear()
            self._loading_character_generation = None
            await self._set_info(
                f"Could not load enhancements for {account}: {error}",
                "#f87171",
            )
            return

        try:
            self.account_history, _ = save_profile(self.settings_path, account)
        except (OSError, ValueError) as error:
            await class_list.clear()
            self._loading_character_generation = None
            message = f"Loaded {account}, but could not save the profile list: {error}"
            if background_startup:
                self.notify(message, severity="error")
            else:
                await self._set_info(message, "#f87171")
            return

        self.account = account
        self._update_character_placeholder()
        self.character_classes = classes.copy()
        self.selected_enhancements = selected_enhancements
        await self._populate_enhancements()
        await class_list.clear()
        self._loading_character_generation = None
        if self.character_classes:
            await class_list.extend(
                ListItem(
                    Horizontal(
                        Static(">", classes="class-marker"),
                        Static(name, classes="class-name"),
                        classes="class-row",
                    ),
                    classes="class-list-item",
                )
                for name in self.character_classes
            )

        if background_startup:
            class_list.index = None
            return

        if not self.character_classes:
            await self._show_commands(f"No classes found for {account}.")
            return

        class_list.index = None
        await self._show_commands(
            f"Loaded {len(self.character_classes)} classes for {account}."
        )

    async def _clear_stale_loading_indicator(self, generation: int) -> None:
        if self._loading_character_generation != generation:
            return
        await self.query_one("#class-list", ListView).clear()
        self._loading_character_generation = None

    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        index = event.list_view.index
        if index is not None and 0 <= index < len(self.character_classes):
            for item in event.list_view.children:
                item.remove_class("selected")
            event.list_view.children[index].add_class("selected")
            await self._show_selected_class(self.character_classes[index])
            if self.nav_mode:
                self._set_nav_pane("left")

    async def _toggle_enhancement(self, button: Button) -> None:
        if self.account is None or button.id is None:
            return
        prefix = "enhancement-"
        if not button.id.startswith(prefix):
            return
        index_text = button.id.removeprefix(prefix)
        if not index_text.isdecimal():
            return
        index = int(index_text)
        if not 0 <= index < len(TOGGLEABLE_ENHANCEMENTS):
            return

        enhancement = TOGGLEABLE_ENHANCEMENTS[index]
        if enhancement in self.selected_enhancements:
            self.selected_enhancements.discard(enhancement)
            indicator = "□"
        else:
            self.selected_enhancements.add(enhancement)
            indicator = "■"
        button.label = f"{indicator} {enhancement}"
        try:
            save_character_enhancements(
                self.settings_path,
                self.account,
                self.selected_enhancements,
            )
        except (OSError, ValueError) as error:
            self.notify(
                f"Could not save enhancements for {self.account}: {error}",
                severity="error",
            )

    async def _populate_enhancements(self) -> None:
        enhancement_list = self.query_one("#enhancements-list", VerticalScroll)
        await enhancement_list.remove_children()
        if self.account is None:
            await enhancement_list.mount(
                Static(
                    "Load a character to choose enhancements.",
                    classes="info-detail",
                )
            )
            return

        await enhancement_list.mount(
            *(
                self._create_enhancement_button(index, name)
                for index, name in enumerate(TOGGLEABLE_ENHANCEMENTS)
            )
        )

    def _create_enhancement_button(self, index: int, name: str) -> Button:
        button = NavButton(
            f"{'■' if name in self.selected_enhancements else '□'} {name}",
            id=f"enhancement-{index}",
            classes="enhancement-toggle",
        )
        button.styles.color = enhancement_color(name)
        return button

    def _show_classes_tab(self) -> None:
        self.nav_tab = "classes"
        self.query_one("#class-list", ListView).display = True
        self.query_one("#enhancements-list", VerticalScroll).display = False
        self._render_tab_title()
        self._sync_nav_cursor()

    def _show_enhancements_tab(self) -> None:
        self.nav_tab = "enhancements"
        self.query_one("#class-list", ListView).display = False
        self.query_one("#enhancements-list", VerticalScroll).display = True
        self._render_tab_title()
        self._sync_nav_cursor()

    def _render_tab_title(self) -> None:
        self.query_one("#class-panel", Vertical).border_title = self._tab_title()

    def _tab_title(self) -> Text:
        title = Text()
        for name, label in (("classes", "Classes"), ("enhancements", "Enhancements")):
            if name == "enhancements":
                title.append(" ─ ", style="#38bdf8")
            if self.nav_mode and self.nav_header and self.nav_header_item == name:
                title.append("> ", style="#FFE3B5")
            active = self.nav_tab == name
            title.append(label, style="bold underline" if active else "#38bdf8")
        return title

    def _tab_at(self, x: int) -> str | None:
        plain = self._tab_title().plain
        for name, label in (("classes", "Classes"), ("enhancements", "Enhancements")):
            start = plain.find(label) + 2
            if start - 2 >= 0 and start <= x < start + len(label):
                return name
        return None

    async def on_click(self, event: Click) -> None:
        class_panel = self.query_one("#class-panel", Vertical)
        if event.widget is class_panel and event.y == 0:
            tab = self._tab_at(event.x)
            if tab == "classes":
                self._show_classes_tab()
            elif tab == "enhancements":
                self._show_enhancements_tab()
            return

        info_panel = self.query_one("#info-panel", Vertical)
        if event.widget is not info_panel or event.y != 0:
            return
        controls = self._info_control_text()
        if not controls:
            return
        control_start = info_panel.size.width - 2 - cell_len(controls)
        back_start = control_start
        back_end = back_start + cell_len(self._info_back_label)
        if self._info_back_enabled and back_start <= event.x < back_end:
            await self.action_navigate_back()
        elif self._info_home_enabled:
            home_start = (
                back_end + cell_len(" | ")
                if self._info_back_enabled
                else control_start
            )
            if home_start <= event.x < home_start + len("Home"):
                await self._show_commands()

    def on_resize(self, _event: Resize) -> None:
        _ = _event
        self._update_info_border_title()

    async def _show_selected_class(self, class_name: str) -> None:
        self._clear_selected_class_data()
        try:
            data = load_class_data(class_name)
        except (OSError, ValueError) as error:
            await self._set_info(
                f"Could not load class data: {error}",
                "#f87171",
                session="Error",
            )
            return

        self.selected_class = class_name
        self.selected_class_data = data
        self._show_class_model_subtitle(data.get("model", ""))
        self.selected_class_file = CLASS_DEFINITIONS_FILE
        self.info_history = []
        self.detail_counter = 0
        await self._show_class_sections()

    def _show_class_model_subtitle(self, model: str) -> None:
        panel = self.query_one("#info-panel", Vertical)
        panel.border_subtitle = Text(model, style="#4ade80") if model else ""
        panel.styles.border_subtitle_align = "center"

    def _clear_selected_class_data(self) -> None:
        self._show_class_model_subtitle("")
        self.selected_class = ""
        self.selected_class_data = {}
        self.selected_class_file = Path()
        self.info_history.clear()
        self.detail_counter = 0

    async def _set_info(
        self,
        message: str,
        color: str = "#d1d5db",
        *,
        session: str = "Info",
    ) -> None:
        panel = self.query_one("#info-panel", Vertical)
        panel.styles.border = ("round", color)
        self._set_info_session(session)
        self._set_back_label("Back")
        self._set_back_enabled(False)
        self._set_home_enabled(False)
        await self._clear_info_content()
        await self.query_one("#info-content", VerticalScroll).mount(
            Static(message, classes="info-detail")
        )

    async def _show_commands(self, status: str | None = None) -> None:
        self._clear_selected_class_data()
        self.query_one("#info-panel", Vertical).styles.border = (
            "round",
            "#4ade80",
        )
        self._set_info_session("Commands")
        self._set_back_label("Back")
        self._set_back_enabled(False)
        self._set_home_enabled(False)
        await self._clear_info_content()
        content = self.query_one("#info-content", VerticalScroll)
        command_width = max(len(command) for command, _ in COMMANDS) + 1
        for command, description in COMMANDS:
            label = Text(f"{command:<{command_width}}", style="#4ade80")
            label.append(description, style="#d1d5db")
            await content.mount(Static(label, classes="info-detail"))
        if status:
            await content.mount(Static(status, classes="info-detail"))

    async def _show_saved_characters(self, status: str | None = None) -> None:
        await self._clear_info_content()
        self._set_info_session("Saved Characters")
        self._set_back_enabled(False)
        self._set_home_enabled(False)
        content = self.query_one("#info-content", VerticalScroll)
        await content.mount(
            Static(
                "Using '/char name' will add a character\n"
                "Example: 'c Potato Lady'\n\n"
                "Using '/char -name' will remove the character\n"
                "Example: 'c -Potato Lady'\n",
                classes="update-warning",
            )
        )
        if status:
            await content.mount(Static(status, classes="info-detail"))
        if not self.account_history:
            await content.mount(
                Static(
                    "No saved characters. Use char NAME to add one.",
                    classes="info-detail",
                )
            )
            return

        for index, account in enumerate(self.account_history):
            await content.mount(
                NavButton(
                    account,
                    id=f"saved-character-{index}",
                    classes="info-action",
                )
            )

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id and button_id.startswith("saved-character-"):
            index_text = button_id.removeprefix("saved-character-")
            if index_text.isdecimal():
                index = int(index_text)
                if 0 <= index < len(self.account_history):
                    await self._load_character(self.account_history[index])
        elif button_id == "update-yes":
            await self._start_release_update()
        elif button_id == "update-no" or button_id == "update-ok":
            await self._show_commands()
        elif button_id == "info-back":
            await self.action_navigate_back()
        elif button_id == "info-home":
            await self._show_commands()
        elif button_id and button_id.startswith("enhancement-"):
            await self._toggle_enhancement(event.button)
        elif button_id == "update-available":
            command_input = self.query_one("#command-input", Input)
            command_input.value = "/update"
            command_input.cursor_position = len(command_input.value)
            command_input.focus()
        elif button_id == "nav-enhancements":
            self.info_history.append("Class")
            await self._show_enhancement_modes()
        elif button_id == "nav-skills":
            self.info_history.append("Class")
            await self._show_skills()
        elif button_id and button_id.startswith("class-model-"):
            index = int(button_id.removeprefix("class-model-"))
            model = CLASS_MODELS[index]
            self.info_history.append("Class Models")
            await self._show_class_model(model)
        elif button_id and button_id.startswith("nav-mode-"):
            mode = button_id.removeprefix("nav-mode-")
            self.info_history.append("Enhancements")
            await self._show_enhancement_mode(mode)
        elif button_id and button_id.startswith("group-"):
            body = self.query_one(f"#{button_id}-body", Vertical)
            body.display = not body.display
            self._sync_nav_cursor()
        elif button_id and button_id.startswith("detail-"):
            self._toggle_detail(button_id)

    async def _show_update_confirmation(self) -> None:
        await self._clear_info_content()
        self._set_info_session("Update")
        self._set_back_enabled(False)
        self._set_home_enabled(False)
        content = self.query_one("#info-content", VerticalScroll)
        await content.mount(
            Static(
                "Synchronize your information with the Git repository?",
                classes="update-warning",
            ),
            Horizontal(
                NavButton("YES", id="update-yes", classes="update-choice"),
                NavButton("NO", id="update-no", classes="update-choice"),
                id="update-choices",
            ),
        )

    async def _start_release_update(self) -> None:
        await self._set_info(
            "Downloading and installing the latest release...",
            "#f87171",
            session="Update",
        )
        self.run_worker(
            self._install_release_update(),
            name="install-latest-release",
            group="release-update",
            exclusive=True,
        )

    async def _install_release_update(self) -> None:
        try:
            tag = await asyncio.to_thread(install_latest_release, sys.executable)
        except NoPublishedReleaseError as error:
            await self._set_info(str(error), "#f87171", session="Update")
        except (OSError, TimeoutError, UnicodeError, ValueError, RuntimeError) as error:
            logger.exception("Could not install the latest AQW Helper release")
            await self._set_info(
                f"Update failed: {error}",
                "#f87171",
                session="Update",
            )
        else:
            logger.info("Release %s installed; restarting AQW Helper", tag)
            self.restart_requested = True
            await self._clear_runtime_cache()
            await super().action_quit()

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        if action in NAV_ACTIONS:
            return self.nav_mode
        return True

    def action_toggle_navigation(self) -> None:
        self._set_nav_mode(not self.nav_mode)

    def _set_nav_mode(self, enabled: bool) -> None:
        self.nav_mode = enabled
        command_input = self.query_one("#command-input", Input)
        class_list = self.query_one("#class-list", ListView)
        self.query_one("#class-panel", Vertical).border_subtitle = (
            "Ctrl + N to disable" if enabled else ""
        )
        command_input.disabled = enabled
        self.nav_header = False
        if enabled:
            if class_list.index is None and class_list.children:
                class_list.index = 0
            self.set_focus(None)
            has_right = bool(class_list.children) or self.nav_tab == "enhancements"
            self._set_nav_pane("right" if has_right else "left")
        else:
            self._set_nav_pane(self.nav_pane)
            command_input.focus()
        self._render_tab_title()

    def _set_nav_pane(self, pane: str) -> None:
        self.nav_pane = pane
        self._sync_nav_cursor()

    def action_nav_toggle_pane(self) -> None:
        class_list = self.query_one("#class-list", ListView)
        has_right = bool(class_list.children) or self.nav_tab == "enhancements"
        if self.nav_pane == "right" or not has_right:
            self._set_nav_pane("left")
        else:
            self._set_nav_pane("right")

    def _nav_buttons(self) -> list[NavButton]:
        content = self.query_one("#info-content", VerticalScroll)
        return [
            button
            for button in content.query(NavButton)
            if button.display
            and all(
                ancestor.display
                for ancestor in button.ancestors
                if ancestor is not content and content in ancestor.ancestors
            )
        ]

    def _enhancement_buttons(self) -> list[NavButton]:
        return list(self.query_one("#enhancements-list", VerticalScroll).query(NavButton))

    def _sync_nav_cursor(self) -> None:
        class_list = self.query_one("#class-list", ListView)
        right_active = self.nav_mode and self.nav_pane == "right"
        class_list.set_class(right_active and not self.nav_header, "nav-active")
        enh_buttons = self._enhancement_buttons()
        self.enh_index = max(0, min(self.enh_index, len(enh_buttons) - 1))
        show_enh = right_active and not self.nav_header and self.nav_tab == "enhancements"
        for position, button in enumerate(enh_buttons):
            button.set_class(show_enh and position == self.enh_index, "nav-cursor")
            button.refresh()
        if show_enh and enh_buttons:
            enh_buttons[self.enh_index].scroll_visible()
        self._render_tab_title()
        buttons = self._nav_buttons()
        if self._nav_button not in buttons:
            self._nav_button = buttons[0] if buttons else None
        show_cursor = self.nav_mode and self.nav_pane == "left"
        for button in self.query_one("#info-content", VerticalScroll).query(NavButton):
            button.set_class(show_cursor and button is self._nav_button, "nav-cursor")
            button.refresh()
        if show_cursor and self._nav_button is not None:
            self._nav_button.scroll_visible()

    def on_nav_button_mounted(self, event: NavButton.Mounted) -> None:
        self.call_after_refresh(self._sync_nav_cursor)

    def _move_nav_button(self, step: int) -> None:
        buttons = self._nav_buttons()
        if not buttons:
            return
        current = buttons.index(self._nav_button) if self._nav_button in buttons else 0
        self._nav_button = buttons[max(0, min(len(buttons) - 1, current + step))]
        self._sync_nav_cursor()

    def _move_right_cursor(self, step: int) -> None:
        if self.nav_header:
            if step > 0:
                self.nav_header = False
        elif self.nav_tab == "enhancements":
            if step < 0 and self.enh_index <= 0:
                self.nav_header = True
                self.nav_header_item = "enhancements"
            else:
                self.enh_index = max(0, self.enh_index + step)
        else:
            class_list = self.query_one("#class-list", ListView)
            if step < 0 and (class_list.index or 0) <= 0:
                self.nav_header = True
                self.nav_header_item = "classes"
            elif step < 0:
                class_list.action_cursor_up()
            else:
                class_list.action_cursor_down()
        self._sync_nav_cursor()

    def action_nav_up(self) -> None:
        if self.nav_pane == "right":
            self._move_right_cursor(-1)
        else:
            self._move_nav_button(-1)

    def action_nav_down(self) -> None:
        if self.nav_pane == "right":
            self._move_right_cursor(1)
        else:
            self._move_nav_button(1)

    def action_nav_select(self) -> None:
        if self.nav_pane == "right":
            if self.nav_header:
                self.nav_header = False
                if self.nav_header_item == "enhancements":
                    self.enh_index = 0
                    self._show_enhancements_tab()
                else:
                    self._show_classes_tab()
            elif self.nav_tab == "enhancements":
                buttons = self._enhancement_buttons()
                if buttons:
                    buttons[self.enh_index].press()
            else:
                self.query_one("#class-list", ListView).action_select_cursor()
        elif self._nav_button is not None:
            self._nav_button.press()

    def _on_nav_header(self) -> bool:
        return self.nav_pane == "right" and self.nav_header

    def action_nav_right(self) -> None:
        if self._on_nav_header():
            self.nav_header_item = "enhancements"
            self._sync_nav_cursor()
        else:
            self.action_nav_select()

    async def action_nav_left(self) -> None:
        if self._on_nav_header():
            self.nav_header_item = "classes"
            self._sync_nav_cursor()
        else:
            await self.action_nav_back()

    async def action_nav_back(self) -> None:
        await self.action_navigate_back()

    def _page_class_list(self, direction: int) -> None:
        if self.nav_tab == "enhancements":
            count = len(self._enhancement_buttons())
            height = self.query_one("#enhancements-list", VerticalScroll).size.height
            self.enh_index = max(0, min(count - 1, self.enh_index + direction * max(1, height)))
            self._sync_nav_cursor()
            return
        class_list = self.query_one("#class-list", ListView)
        count = len(class_list.children)
        if not count:
            return
        step = max(1, class_list.size.height)
        current = class_list.index or 0
        class_list.index = max(0, min(count - 1, current + direction * step))

    def action_scroll_info_up(self) -> None:
        if self.nav_mode and self.nav_pane == "right":
            self._page_class_list(-1)
            return
        self.query_one("#info-content", VerticalScroll).scroll_page_up()

    def action_scroll_info_down(self) -> None:
        if self.nav_mode and self.nav_pane == "right":
            self._page_class_list(1)
            return
        self.query_one("#info-content", VerticalScroll).scroll_page_down()

    async def action_navigate_back(self) -> None:
        if not self.info_history:
            await self._show_commands()
            return

        previous = self.info_history.pop()
        if previous == "Class":
            await self._show_class_sections()
        elif previous == "Enhancements":
            await self._show_enhancement_modes()
        elif previous == "Class Models":
            await self._show_stats()

    def _set_info_session(self, session: str) -> None:
        self._info_panel_title = session
        self._update_info_border_title()

    def _set_back_enabled(self, enabled: bool) -> None:
        self._info_back_enabled = enabled
        self._update_info_border_title()

    def _set_home_enabled(self, enabled: bool) -> None:
        self._info_home_enabled = enabled
        self._update_info_border_title()

    def _set_back_label(self, label: str) -> None:
        self._info_back_label = f"← {label}"
        self._update_info_border_title()

    def _info_control_text(self) -> str:
        controls = self._info_back_label if self._info_back_enabled else ""
        if self._info_back_enabled and self._info_home_enabled:
            controls += " | "
        if self._info_home_enabled:
            controls += "Home"
        return controls

    def _update_info_border_title(self) -> None:
        panel = self.query_one("#info-panel", Vertical)
        controls = self._info_control_text()
        if not controls:
            panel.border_title = self._info_panel_title
            return

        title = Text(self._info_panel_title, style="#4ade80")
        spacer_width = max(
            1,
            panel.size.width
            - 4
            - cell_len(self._info_panel_title)
            - cell_len(controls)
            - 2,
        )
        title.append(" ", style="#4ade80")
        title.append("─" * spacer_width, style="#4ade80")
        title.append(" ", style="#4ade80")
        if self._info_back_enabled:
            title.append(self._info_back_label, style="bold #4ade80")
        if self._info_back_enabled and self._info_home_enabled:
            title.append(" | ", style="#4ade80")
        if self._info_home_enabled:
            title.append("Home", style="bold #4ade80")
        self.query_one("#info-panel", Vertical).border_title = title

    async def _clear_info_content(self) -> None:
        await self.query_one("#info-content", VerticalScroll).remove_children()

    async def _mount_class_description(self, content: VerticalScroll) -> None:
        description = self.selected_class_data.get("description")
        if description:
            await content.mount(
                Static(
                    style_description(description),
                    classes="info-detail class-description",
                ),
            )

    async def _show_class_sections(self) -> None:
        self.query_one("#info-panel", Vertical).styles.border = (
            "round",
            "#4ade80",
        )
        self._set_info_session(self.selected_class)
        self._set_back_enabled(False)
        self._set_home_enabled(True)
        await self._clear_info_content()
        content = self.query_one("#info-content", VerticalScroll)
        await self._mount_class_description(content)
        await content.mount(
            NavButton("Enhancements", id="nav-enhancements", classes="info-action"),
            NavButton("Skills", id="nav-skills", classes="info-action"),
        )

    async def _show_enhancement_modes(self) -> None:
        await self._clear_info_content()
        self._set_info_session(self.selected_class)
        self._set_back_label("Back")
        self._set_back_enabled(True)
        self._set_home_enabled(True)
        content = self.query_one("#info-content", VerticalScroll)
        await self._mount_class_description(content)
        await content.mount(
            *(
                NavButton(
                    mode,
                    id=f"nav-mode-{mode}",
                    classes="info-action",
                )
                for mode in ENHANCEMENT_MODES
            )
        )

    async def _show_enhancement_mode(self, mode: str) -> None:
        await self._clear_info_content()
        self._set_info_session(self.selected_class)
        self._set_back_label("Back")
        self._set_back_enabled(True)
        self._set_home_enabled(True)
        content = self.query_one("#info-content", VerticalScroll)
        for slot in ENHANCEMENT_SLOTS:
            await content.mount(Static(slot, classes="enhancement-category"))
            options = resolve_enhancements(
                self.selected_class_data["enhancements"][mode][slot],
                self.selected_enhancements,
            )
            for option, field in options:
                name = field["type"].strip() or "Type"
                label = Text(f"  {option.title()}: ")
                label.append(name, style=enhancement_color(name))
                if option == "base":
                    label.append(" (!)", style="#ff0000")
                await self._mount_detail(
                    content,
                    label,
                    enhancement_info(field["type"].strip()),
                    detail_class="info-detail enhancement-info-detail",
                )
            await content.mount(Static("", classes="enhancement-spacer"))
        potions = self.selected_class_data["enhancements"][mode]["Potions"]
        await self._mount_detail(
            content,
            "Potions",
            "\n".join(
                f"{potion}: {potions[potion]}"
                for potion in ("Tonic", "Elixir", "Potion")
            ),
        )

    async def _show_enhancement_catalog(self) -> None:
        await self._show_catalog_page("Enhancements")
        content = self.query_one("#info-content", VerticalScroll)
        for index, (group, names) in enumerate(ENHANCEMENT_GROUPS):
            group_id = f"group-{index}"
            body = Vertical(id=f"{group_id}-body", classes="enhancement-group")
            await content.mount(
                NavButton(group, id=group_id, classes="info-action group-toggle"),
                body,
            )
            body.display = False
            for name in names:
                await self._mount_detail(
                    body,
                    Text(name, style=enhancement_color(name)),
                    enhancement_info(name),
                    empty_message="No enhancement details yet.",
                )

    async def _show_stats(self) -> None:
        await self._show_catalog_page("Stats - Class Models")
        content = self.query_one("#info-content", VerticalScroll)
        for index, name in enumerate(CLASS_MODELS):
            await content.mount(
                NavButton(
                    Text(name, style=CLASS_MODEL_COLORS[name]),
                    id=f"class-model-{index}",
                    classes="info-action",
                )
            )

    async def _show_class_model(self, name: str) -> None:
        await self._clear_info_content()
        self._set_info_session(f"Stats - {name}")
        self._set_back_label("Back")
        self._set_back_enabled(True)
        self._set_home_enabled(True)
        description = CLASS_MODEL_DESCRIPTIONS[name] or "No description yet."
        await self.query_one("#info-content", VerticalScroll).mount(
            Static(description, classes="info-detail")
        )

    async def _show_advanced(self) -> None:
        await self._show_catalog_page("Advanced")
        content = self.query_one("#info-content", VerticalScroll)
        shortcuts = (
            ("  Ctrl+A  ", "Show this navigation helper"),
            ("  Ctrl+C  ", "Display Characters list"),
            ("  Ctrl+E  ", "Show Enhancements page"),
            ("  Ctrl+R  ", "Reload the program"),
            ("  Ctrl+S  ", "Show Stats page"),
            ("  Ctrl+U  ", "Run Update"),
            ("  Ctrl+X  ", "Return to Home screen"),
            ("  Ctrl+Z  ", "Go back to previous screen"),
            ("  Ctrl+N  ", "Toggle Navigation mode"),
            ("  Tab     ", "Swap windows (Navigation)"),
            ("  PgUp    ", "Scroll the panel up"),
            ("  PgDn    ", "Scroll the panel down"),
            ("  Escape  ", "Close the app"),
        )
        for key, description in shortcuts:
            label = Text(f"{key:<8}", style="#4ade80")
            label.append(description, style="#d1d5db")
            await content.mount(Static(label, classes="info-detail"))

    async def _show_catalog_page(self, title: str) -> None:
        self._clear_selected_class_data()
        self.query_one("#info-panel", Vertical).styles.border = (
            "round",
            "#4ade80",
        )
        self._set_info_session(title)
        self._set_back_label("Back")
        self._set_back_enabled(False)
        self._set_home_enabled(True)
        self.detail_counter = 0
        await self._clear_info_content()

    async def _show_skills(self) -> None:
        await self._clear_info_content()
        self._set_info_session(self.selected_class)
        self._set_back_label("Back")
        self._set_back_enabled(True)
        self._set_home_enabled(True)
        content = self.query_one("#info-content", VerticalScroll)
        for number, skill in enumerate(self.selected_class_data["skills"], start=1):
            name = skill["name"].strip() or f"Skill {number}"
            await self._mount_detail(content, name, skill["info"])

        for number, passive in enumerate(
            self.selected_class_data["passives"], start=1
        ):
            has_value = bool(passive["name"].strip() or passive["info"])
            name = passive["name"].strip() or f"Passive {number}"
            details = passive["info"]
            if number <= 2 or has_value:
                await self._mount_detail(content, name, details)

    async def _mount_detail(
        self,
        content: Vertical | VerticalScroll,
        label: str | Text,
        details: str | list[dict[str, str]],
        *,
        empty_message: str | None = None,
        detail_class: str = "info-detail",
    ) -> None:
        button_id = f"detail-{self.detail_counter}"
        self.detail_counter += 1
        detail = details or empty_message or (
            f"No details yet. Edit {self.selected_class_file}."
        )
        await content.mount(
            NavButton(label, id=button_id, classes="info-action detail-toggle"),
            Static(
                style_description(detail),
                classes=detail_class,
                id=f"{button_id}-text",
            ),
        )
        self.query_one(f"#{button_id}-text", Static).display = False

    def _toggle_detail(self, button_id: str) -> None:
        detail = self.query_one(f"#{button_id}-text", Static)
        detail.display = not detail.display
        self._sync_nav_cursor()


def main() -> None:
    argparse.ArgumentParser(
        description="Open the Linux Console terminal interface."
    ).parse_args()
    app = LinuxConsoleApp()
    app.run(mouse=True)
    if app.restart_requested:
        os.execv(
            sys.executable,
            [sys.executable, "-m", "linux_console", *sys.argv[1:]],
        )
