from __future__ import annotations

import argparse
import asyncio
import logging
import os
import re
from pathlib import Path
import sys
from typing import Any

from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.events import Key
from textual.suggester import Suggester
from textual.widgets import Button, Input, ListItem, ListView, Static

from linux_console.aqw import (
    config_path,
    fetch_classes,
    load_account_history,
    load_default_account,
    remove_saved_account,
    save_default_account,
)
from linux_console.class_data import (
    ENHANCEMENT_MODES,
    ENHANCEMENT_SLOTS,
    class_data_directory,
    class_data_names,
    load_or_create_class_data,
)
from linux_console.version_check import current_version, update_available
from linux_console.release_update import (
    NoPublishedReleaseError,
    install_latest_release,
)

logger = logging.getLogger(__name__)
COMMANDS = (
    ("char", "Load and save a character account."),
    ("reload", "Reload the current character's classes."),
    ("class", "Display any class, owned or not."),
    ("return", "Return to the Commands home page."),
    ("update", "Update the app."),
    ("quit", "Close the app."),
)
COMMAND_ALIASES = {
    "ch": "char",
    "character": "char",
    "q": "quit",
    "r": "return",
    "rl": "reload",
    "up": "update",
    "cl": "class",
    "classes": "class",
}


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
    }

    #info-navigation {
        height: 3;
        dock: top;
        align-vertical: middle;
    }

    #info-back {
        width: auto;
        min-width: 0;
        height: 1;
        padding: 0;
        color: #4ade80;
        background: transparent;
        border: none;
    }

    #info-nav-separator {
        width: auto;
        height: 1;
        padding: 0 1;
        color: #4ade80;
        display: none;
    }

    #info-home {
        width: auto;
        min-width: 0;
        height: 1;
        padding: 0;
        color: #4ade80;
        background: transparent;
        border: none;
        display: none;
    }

    #info-session {
        width: 1fr;
        text-align: left;
        color: #4ade80;
        content-align: left middle;
    }

    #info-content {
        height: 1fr;
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

    .info-detail {
        width: 1fr;
        padding: 0 0 1 0;
        color: #d1d5db;
        text-align: left;
        content-align: left top;
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
        width: 1fr;
        height: 1fr;
        background: #050608;
        border: round #38bdf8;
    }

    .class-name {
        color: #38bdf8;
    }

    #command-input {
        height: 3;
        color: #f87171;
        background: #020403;
        border: round #b91c1c;
    }
    """
    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
        ("ctrl+q", "ignore_quit", "Ignore quit"),
    ]

    def __init__(
        self,
        *,
        settings_path: Path | None = None,
        class_data_path: Path | None = None,
    ) -> None:
        super().__init__()
        self.settings_path = settings_path or config_path()
        self.class_data_path = class_data_path or class_data_directory()
        self.account: str | None = None
        self.character_classes: list[str] = []
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

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Horizontal(
                Static(
                "  █████╗  ██████╗ ██╗    ██╗    ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗\n"
                " ██╔══██╗██╔═══██╗██║    ██║    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗\n"
                " ███████║██║   ██║██║ █╗ ██║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝\n"
                " ██╔══██║██║▄▄ ██║██║███╗██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗\n"
                " ██║  ██║╚██████╔╝╚███╔███╔╝    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║\n"
                " ╚═╝  ╚═╝ ╚══▀▀═╝  ╚══╝╚══╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝",
                    id="banner",
                ),
                Static(f"v.{current_version()}", id="version-label"),
                id="header",
            )
            with Horizontal(id="panels"):
                with Vertical(id="info-panel"):
                    with Horizontal(id="info-navigation"):
                        yield Static("Commands", id="info-session")
                        yield Button("← Back", id="info-back")
                        yield Static("|", id="info-nav-separator")
                        yield Button("Home", id="info-home")
                    yield VerticalScroll(id="info-content")
                    yield Button(
                        "↓ Update Pending",
                        id="update-available",
                        tooltip="Type /update to install the latest release",
                    )
                yield ListView(id="class-list")
            yield Input(
                placeholder="Tab/Right complete · Up/Down cycle",
                id="command-input",
                suggester=CommandSuggester(self),
            )

    async def on_mount(self) -> None:
        self.query_one("#info-panel", Vertical).border_title = "Info"
        self.class_list = self.query_one("#class-list", ListView)
        self.class_list.border_title = "Class"
        await self._clear_runtime_cache()
        self.query_one("#command-input", Input).focus()
        self._set_info_session("Commands")
        self._set_back_enabled(False)
        self._set_home_enabled(False)
        await self._show_commands()
        self.run_worker(
            self._check_for_updates(),
            name="check-for-updates",
            group="update-check",
        )

        try:
            self.account_history = load_account_history(self.settings_path)
            account = load_default_account(self.settings_path)
        except (OSError, ValueError) as error:
            await self._set_info(f"Could not read saved account: {error}", "#f87171")
            return

        if account is None:
            return
        if account.casefold() not in {
            saved.casefold() for saved in self.account_history
        }:
            self.account_history.append(account)
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

    async def action_quit(self) -> None:
        await self._clear_runtime_cache()
        await super().action_quit()

    async def _clear_runtime_cache(self) -> None:
        self.account = None
        self.character_classes.clear()
        self._clear_selected_class_data()
        self.account_history.clear()
        self._completion_cycle = None
        self._programmatic_completion = None
        self._character_load_generation += 1
        self._loading_character_generation = None
        class_list = self.query_one("#class-list", ListView)
        class_list.border_title = "Class"
        await class_list.clear()

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
            candidates = class_data_names(self.class_data_path)
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
        command_names = [command for command, _ in COMMANDS]
        for command in command_names:
            if command.casefold().startswith(command_prefix.casefold()):
                suggestion = f"/{command}" if has_leading_slash else command
                if command.casefold() == command_prefix.casefold():
                    return f"{suggestion} "
                return suggestion
        return None

    async def on_input_submitted(self, event: Input.Submitted) -> None:
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
                    removed = remove_saved_account(
                        self.settings_path,
                        account_name,
                    )
                except (OSError, ValueError) as error:
                    await self._set_info(
                        f"Could not remove {account_name}: {error}",
                        "#f87171",
                    )
                    return
                self.account_history = [
                    saved
                    for saved in self.account_history
                    if saved.casefold() != account_name.casefold()
                ]
                status = (
                    f"Removed {account_name} from saved characters."
                    if removed
                    else f"{account_name} was not in saved characters."
                )
                await self._show_saved_characters(status)
                return
            await self._load_character(argument, save_account=True)
        elif command == "reload":
            if argument:
                await self._set_info("Usage: reload", "#f87171")
            elif self.account is None:
                await self._set_info("Set a character first with char NAME.", "#f87171")
            else:
                await self._load_character(self.account)
        elif command == "class":
            if not argument:
                await self._set_info("Usage: class NAME", "#f87171")
            else:
                await self._show_selected_class(argument)
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
        elif command == "quit":
            if argument:
                await self._set_info("Usage: quit", "#f87171")
            else:
                await self.action_quit()

    async def _load_character(
        self,
        account: str,
        *,
        save_account: bool = False,
        background_startup: bool = False,
    ) -> None:
        self._character_load_generation += 1
        generation = self._character_load_generation
        self.character_classes = []
        class_list = self.query_one("#class-list", ListView)
        class_list.border_title = account
        await class_list.clear()
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
        self.account = account
        self.character_classes = classes.copy()
        await class_list.clear()
        self._loading_character_generation = None
        if self.character_classes:
            await class_list.extend(
                ListItem(Static(name, classes="class-name"))
                for name in self.character_classes
            )

        if save_account:
            try:
                save_default_account(self.settings_path, account)
            except OSError as error:
                if background_startup:
                    self.notify(
                        f"Loaded {account}, but could not save it as default: {error}",
                        severity="error",
                    )
                else:
                    await self._set_info(
                        f"Loaded {account}, but could not save it as default: {error}",
                        "#f87171",
                    )
                return
            self.account_history = [
                saved
                for saved in self.account_history
                if saved.casefold() != account.casefold()
            ]
            self.account_history.append(account)

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
            await self._show_selected_class(self.character_classes[index])

    async def _show_selected_class(self, class_name: str) -> None:
        self._clear_selected_class_data()
        try:
            data, path = load_or_create_class_data(class_name, self.class_data_path)
        except (OSError, ValueError) as error:
            await self._set_info(
                f"Could not load class data: {error}",
                "#f87171",
                session="Error",
            )
            return

        self.selected_class = class_name
        self.selected_class_data = data
        self.selected_class_file = path
        self.info_history = []
        self.detail_counter = 0
        await self._show_class_sections()

    def _clear_selected_class_data(self) -> None:
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
        for command, description in COMMANDS:
            label = Text(f"/{command:<11}", style="#4ade80")
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
                "Using '/char -' will remove the character\n"
                "Example: 'char -Potato Lady'\n",
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
                Button(
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
            await self._navigate_back()
        elif button_id == "info-home":
            await self._show_commands()
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
        elif button_id and button_id.startswith("nav-mode-"):
            mode = button_id.removeprefix("nav-mode-")
            self.info_history.append("Enhancements")
            await self._show_enhancement_mode(mode)
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
                Button("YES", id="update-yes", classes="update-choice"),
                Button("NO", id="update-no", classes="update-choice"),
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

    async def _navigate_back(self) -> None:
        if not self.info_history:
            await self._show_commands()
            return

        previous = self.info_history.pop()
        if previous == "Class":
            await self._show_class_sections()
        elif previous == "Enhancements":
            await self._show_enhancement_modes()

    def _set_info_session(self, session: str) -> None:
        self.query_one("#info-session", Static).update(session)

    def _set_back_enabled(self, enabled: bool) -> None:
        back_button = self.query_one("#info-back", Button)
        back_button.disabled = not enabled
        back_button.display = enabled
        self.query_one("#info-nav-separator", Static).display = (
            enabled and self.query_one("#info-home", Button).display
        )

    def _set_home_enabled(self, enabled: bool) -> None:
        self.query_one("#info-home", Button).display = enabled
        self.query_one("#info-nav-separator", Static).display = (
            enabled and self.query_one("#info-back", Button).display
        )

    def _set_back_label(self, label: str) -> None:
        self.query_one("#info-back", Button).label = f"← {label}"

    async def _clear_info_content(self) -> None:
        await self.query_one("#info-content", VerticalScroll).remove_children()

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
        await content.mount(
            Button("Enhancements", id="nav-enhancements", classes="info-action"),
            Button("Skills", id="nav-skills", classes="info-action"),
        )

    async def _show_enhancement_modes(self) -> None:
        await self._clear_info_content()
        self._set_info_session("Enhancements")
        self._set_back_label("Back")
        self._set_back_enabled(True)
        self._set_home_enabled(True)
        content = self.query_one("#info-content", VerticalScroll)
        await content.mount(
            *(
                Button(
                    mode,
                    id=f"nav-mode-{mode}",
                    classes="info-action",
                )
                for mode in ENHANCEMENT_MODES
            )
        )

    async def _show_enhancement_mode(self, mode: str) -> None:
        await self._clear_info_content()
        self._set_info_session(mode)
        self._set_back_label("Back")
        self._set_back_enabled(True)
        self._set_home_enabled(True)
        content = self.query_one("#info-content", VerticalScroll)
        for slot in ENHANCEMENT_SLOTS:
            field = self.selected_class_data["enhancements"][mode][slot]
            label = f"{slot}: {field['type'].strip() or 'Type'}"
            await self._mount_detail(content, label, field["info"].strip())

    async def _show_skills(self) -> None:
        await self._clear_info_content()
        self._set_info_session("Skills")
        self._set_back_label("Back")
        self._set_back_enabled(True)
        self._set_home_enabled(True)
        content = self.query_one("#info-content", VerticalScroll)
        for number, skill in enumerate(self.selected_class_data["skills"], start=1):
            name = skill["name"].strip() or f"Skill {number}"
            await self._mount_detail(content, name, skill["info"].strip())

        for number, passive in enumerate(
            self.selected_class_data["passives"], start=1
        ):
            has_value = bool(passive["name"].strip() or passive["info"].strip())
            name = passive["name"].strip() or f"Passive {number}"
            details = passive["info"].strip()
            if number <= 2 or has_value:
                await self._mount_detail(content, name, details)

    async def _mount_detail(
        self, content: VerticalScroll, label: str, details: str
    ) -> None:
        button_id = f"detail-{self.detail_counter}"
        self.detail_counter += 1
        detail = details or f"No details yet. Edit {self.selected_class_file}."
        await content.mount(
            Button(label, id=button_id, classes="info-action detail-toggle"),
            Static(
                detail,
                classes="info-detail",
                id=f"{button_id}-text",
            ),
        )
        self.query_one(f"#{button_id}-text", Static).display = False

    def _toggle_detail(self, button_id: str) -> None:
        detail = self.query_one(f"#{button_id}-text", Static)
        detail.display = not detail.display


def main() -> None:
    argparse.ArgumentParser(
        description="Open the Linux Console terminal interface."
    ).parse_args()
    app = LinuxConsoleApp()
    app.run()
    if app.restart_requested:
        os.execv(
            sys.executable,
            [sys.executable, "-m", "linux_console", *sys.argv[1:]],
        )
