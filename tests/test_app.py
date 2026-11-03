import asyncio
import json
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

from textual.containers import Vertical
from textual.widgets import Button, Footer, Input, ListView, Static

from linux_console.app import LinuxConsoleApp
from linux_console.aqw import save_default_account
from linux_console.class_data import (
    class_data_path,
    load_or_create_class_data,
)


class LinuxConsoleAppTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        update_check_patcher = patch(
            "linux_console.app.update_available",
            return_value=False,
        )
        update_check_patcher.start()
        self.addCleanup(update_check_patcher.stop)

    async def test_update_icon_pastes_command_without_executing_it(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            with patch("linux_console.app.update_available", return_value=True):
                app = LinuxConsoleApp(
                    settings_path=Path(temporary_directory) / "config.json",
                    class_data_path=Path(temporary_directory) / "classes",
                )
                async with app.run_test() as pilot:
                    update_button = app.query_one("#update-available", Button)
                    await pilot.pause()
                    self.assertTrue(update_button.display)

                    await pilot.click("#update-available")
                    await pilot.pause()

                    command_input = app.query_one("#command-input", Input)
                    self.assertEqual(command_input.value, "/update")
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Commands",
                    )

    async def test_char_without_argument_lists_and_loads_saved_characters(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            settings_path = temporary_path / "config.json"
            save_default_account(settings_path, "Older Character")
            save_default_account(settings_path, "Latest Character")

            def classes_for(account: str) -> list[str]:
                return {
                    "Older Character": ["Arachnomancer"],
                    "Latest Character": ["Dragon of Time"],
                }[account]

            with patch(
                "linux_console.app.fetch_classes",
                side_effect=classes_for,
            ) as fetch:
                app = LinuxConsoleApp(
                    settings_path=settings_path,
                    class_data_path=temporary_path / "classes",
                )
                async with app.run_test() as pilot:
                    command_input = app.query_one("#command-input", Input)
                    command_input.value = "/char"
                    await pilot.press("enter")
                    await pilot.pause()

                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Saved Characters",
                    )
                    self.assertEqual(
                        [button.label for button in app.query("#info-content Button")],
                        ["Older Character", "Latest Character"],
                    )

                    await pilot.click("#saved-character-0")
                    await pilot.pause()

                    self.assertEqual(
                        [call.args[0] for call in fetch.call_args_list],
                        ["Latest Character", "Older Character"],
                    )
                    self.assertEqual(
                        app.query_one("#class-list", ListView).border_title,
                        "Older Character",
                    )
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Commands",
                    )
                    self.assertEqual(
                        list(app.query("#info-content Button")),
                        [],
                    )
                    self.assertIn(
                        "Loaded 1 classes for Older Character.",
                        " ".join(
                            str(widget.render())
                            for widget in app.query("#info-content Static")
                        ),
                    )

    async def test_startup_screen_renders_before_saved_character_load_finishes(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            settings_path = temporary_path / "config.json"
            settings_path.write_text('{"account":"Potato Lady"}', encoding="utf-8")
            fetch_started = threading.Event()
            release_fetch = threading.Event()

            def delayed_fetch(_account: str) -> list[str]:
                self.assertEqual(_account, "Potato Lady")
                fetch_started.set()
                release_fetch.wait(timeout=3)
                return ["Arachnomancer"]

            with patch(
                "linux_console.app.fetch_classes",
                side_effect=delayed_fetch,
            ):
                app = LinuxConsoleApp(
                    settings_path=settings_path,
                    class_data_path=temporary_path / "classes",
                )
                async with app.run_test() as pilot:
                    self.assertTrue(await asyncio.to_thread(fetch_started.wait, 1))
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Commands",
                    )
                    self.assertIsNotNone(app.query_one("#command-input", Input))
                    class_list = app.query_one("#class-list", ListView)
                    self.assertEqual(
                        len(class_list.children),
                        1,
                    )
                    self.assertEqual(
                        str(class_list.children[0].query_one(Static).render()),
                        "Loading...",
                    )

                    command_input = app.query_one("#command-input", Input)
                    command_input.value = "/class Dragon of Time"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Dragon of Time",
                    )

                    release_fetch.set()
                    await pilot.pause(0.2)
                    self.assertEqual(
                        len(app.query_one("#class-list", ListView).children),
                        1,
                    )
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Dragon of Time",
                    )
                release_fetch.set()

    async def test_ctrl_q_does_not_quit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            app = LinuxConsoleApp(
                settings_path=Path(temporary_directory) / "config.json",
                class_data_path=Path(temporary_directory) / "classes",
            )
            async with app.run_test() as pilot:
                await pilot.press("ctrl+q")
                await pilot.pause()
                self.assertTrue(app.is_running)

    async def test_char_minus_name_removes_saved_character(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            settings_path = temporary_path / "config.json"
            save_default_account(settings_path, "Older Character")
            save_default_account(settings_path, "Latest Character")

            with patch(
                "linux_console.app.fetch_classes",
                return_value=["Arachnomancer"],
            ):
                app = LinuxConsoleApp(
                    settings_path=settings_path,
                    class_data_path=temporary_path / "classes",
                )
                async with app.run_test() as pilot:
                    command_input = app.query_one("#command-input", Input)
                    command_input.value = "/char"
                    await pilot.press("enter")
                    await pilot.pause()

                    self.assertIn(
                        "Using /char -NAME will remove the character",
                        " ".join(
                            str(widget.render())
                            for widget in app.query("#info-content Static")
                        ),
                    )

                    command_input.focus()
                    command_input.value = "/char -Older Character"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(
                        [button.label for button in app.query("#info-content Button")],
                        ["Latest Character"],
                    )
                    self.assertIn(
                        "Removed Older Character",
                        " ".join(
                            str(widget.render())
                            for widget in app.query("#info-content Static")
                        ),
                    )

                    command_input.focus()
                    command_input.value = "/char -Latest Character"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(
                        list(app.query("#info-content Button")),
                        [],
                    )
                    self.assertIn(
                        "No saved characters",
                        " ".join(
                            str(widget.render())
                            for widget in app.query("#info-content Static")
                        ),
                    )
                    saved_config = json.loads(settings_path.read_text(encoding="utf-8"))
                    self.assertNotIn("account", saved_config)
                    self.assertEqual(saved_config["account_history"], [])

    async def test_command_autocomplete_and_candidate_cycling(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            settings_path = temporary_path / "config.json"
            class_directory = temporary_path / "classes"
            save_default_account(settings_path, "Older Character")
            save_default_account(settings_path, "Latest Character")
            load_or_create_class_data("Arachnomancer", class_directory)
            load_or_create_class_data("Dragon of Time", class_directory)

            with patch("linux_console.app.fetch_classes", return_value=[]):
                app = LinuxConsoleApp(
                    settings_path=settings_path,
                    class_data_path=class_directory,
                )
                async with app.run_test() as pilot:
                    command_input = app.query_one("#command-input", Input)
                    command_input.focus()
                    command_input.value = "/char "
                    await pilot.pause()
                    await pilot.press("tab")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/char Latest Character ")

                    command_input.value = "/char "
                    await pilot.pause()
                    await pilot.press("up")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/char Latest Character")
                    await pilot.press("up")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/char Older Character")
                    await pilot.press("down")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/char Latest Character")

                    command_input.value = "/cl"
                    await pilot.pause()
                    await pilot.press("tab")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/class ")

                    command_input.value = "/ch"
                    await pilot.pause()
                    await pilot.press("tab")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/char ")

                    command_input.value = "/class "
                    await pilot.pause()
                    await pilot.press("tab")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/class Arachnomancer ")

                    command_input.value = "/class "
                    await pilot.pause()
                    await pilot.press("up")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/class Arachnomancer")
                    await pilot.press("up")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/class Dragon of Time")
                    await pilot.press("down")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/class Arachnomancer")

                    command_input.value = "/class Ara"
                    await pilot.pause()
                    await pilot.press("right")
                    await pilot.pause()
                    self.assertEqual(command_input.value, "/class Arachnomancer")

                    command_input.value = "char Newly Used Character"
                    await pilot.press("enter")
                    await pilot.pause()
                    saved_config = json.loads(settings_path.read_text(encoding="utf-8"))
                    self.assertEqual(
                        saved_config["account_history"][-1],
                        "Newly Used Character",
                    )

    async def test_short_and_long_command_aliases(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            class_directory = temporary_path / "classes"
            with patch(
                "linux_console.app.fetch_classes",
                return_value=["Arachnomancer"],
            ) as fetch:
                app = LinuxConsoleApp(
                    settings_path=temporary_path / "config.json",
                    class_data_path=class_directory,
                )
                async with app.run_test() as pilot:
                    command_input = app.query_one("#command-input", Input)
                    for alias, account in (
                        ("/ch", "Potato Lady"),
                        ("/character", "Another Character"),
                    ):
                        command_input.focus()
                        command_input.value = f"{alias} {account}"
                        await pilot.press("enter")
                        await pilot.pause()

                    self.assertEqual(
                        [call.args[0] for call in fetch.call_args_list],
                        ["Potato Lady", "Another Character"],
                    )

                    command_input.focus()
                    command_input.value = "/class Arachnomancer"
                    await pilot.press("enter")
                    await pilot.pause()
                    command_input.focus()
                    command_input.value = "/r"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(fetch.call_count, 2)
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Commands",
                    )

                    command_input.focus()
                    command_input.value = "/rl"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(fetch.call_count, 3)
                    self.assertEqual(fetch.call_args.args[0], "Another Character")
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Commands",
                    )

                    command_input.value = "/class Arachnomancer"
                    await pilot.press("enter")
                    await pilot.pause()
                    command_input.value = "/char Potato Lady"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(fetch.call_count, 4)
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Commands",
                    )

                    command_input.value = "/return"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(
                        str(
                            app.query_one("#info-session", Static).render()
                        ).strip(),
                        "Commands",
                    )

                    for alias in ("/cl", "/classes"):
                        command_input.focus()
                        command_input.value = f"{alias} Arachnomancer"
                        await pilot.press("enter")
                        await pilot.pause()
                        self.assertEqual(
                            str(
                                app.query_one("#info-session", Static).render()
                            ).strip(),
                            "Arachnomancer",
                        )

                    command_input.focus()
                    command_input.value = "/up"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertTrue(app.query_one("#update-yes", Button))

    async def test_class_navigation_and_expandable_details(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            class_directory = temporary_path / "classes"
            class_name = "Arachnomancer"
            data_file = class_data_path(class_name, class_directory)

            with patch(
                "linux_console.app.fetch_classes",
                return_value=[class_name, "Arcana Invoker"],
            ) as fetch:
                app = LinuxConsoleApp(
                    settings_path=temporary_path / "config.json",
                    class_data_path=class_directory,
                )
                async with app.run_test(size=(120, 60)) as pilot:
                    info_panel = app.query_one("#info-panel", Vertical)
                    self.assertEqual(info_panel.border_title, "Info")
                    self.assertEqual(len(app.query(Button)), 3)
                    self.assertEqual(len(app.query(Footer)), 0)
                    self.assertFalse(app.query_one("#info-back", Button).display)
                    self.assertFalse(app.query_one("#info-home", Button).display)
                    self.assertEqual(
                        str(app.query_one("#info-session", Static).render()).strip(),
                        "Commands",
                    )
                    self.assertFalse(
                        any(
                            str(widget.render()).strip() == "Commands"
                            for widget in app.query("#info-content Static")
                        )
                    )

                    command_input = app.query_one("#command-input", Input)
                    command_input.value = "char Potato Lady"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertEqual(fetch.call_args.args, ("Potato Lady",))
                    self.assertEqual(
                        app.query_one("#class-list", ListView).border_title,
                        "Potato Lady",
                    )
                    self.assertTrue(
                        any(
                            "Loaded 2 classes" in str(widget.render())
                            for widget in app.query("#info-content Static")
                        )
                    )

                    class_list = app.query_one("#class-list", ListView)
                    class_list.index = 0
                    class_list.action_select_cursor()
                    await pilot.pause()
                    self.assertEqual(
                        str(app.query_one("#info-session", Static).render()).strip(),
                        class_name,
                    )
                    self.assertEqual(
                        [button.label for button in app.query("#info-content Button")],
                        ["Enhancements", "Skills"],
                    )
                    info_content = app.query_one("#info-content")
                    self.assertTrue(
                        all(
                            button.region.x == info_content.region.x
                            for button in app.query("#info-content Button")
                        )
                    )
                    help_button = app.query_one("#info-back", Button)
                    home_button = app.query_one("#info-home", Button)
                    self.assertEqual(home_button.label, "Home")
                    self.assertFalse(help_button.display)
                    self.assertTrue(home_button.display)
                    session_label = app.query_one("#info-session", Static)
                    self.assertLess(
                        session_label.region.x,
                        home_button.region.x,
                    )
                    self.assertEqual(session_label.styles.text_align, "left")
                    await pilot.click("#info-home")
                    await pilot.pause()
                    self.assertFalse(help_button.display)
                    self.assertFalse(home_button.display)
                    self.assertEqual(app.selected_class, "")
                    self.assertEqual(app.selected_class_data, {})
                    self.assertEqual(app.selected_class_file, Path())
                    self.assertEqual(
                        str(app.query_one("#info-session", Static).render()).strip(),
                        "Commands",
                    )
                    command_input.focus()
                    command_input.value = "class Arachnomancer"
                    await pilot.press("enter")
                    await pilot.pause()
                    self.assertTrue(data_file.exists())
                    self.assertFalse(
                        any(
                            "Class:" in str(button.label)
                            for button in app.query("#info-content Button")
                        )
                    )

                    data = json.loads(data_file.read_text(encoding="utf-8"))
                    data["enhancements"]["Solo"]["Class"] = {
                        "type": "Lucky",
                        "info": "Improves critical chance.",
                    }
                    data["skills"][0] = {
                        "name": "Venom Strike",
                        "info": "Deals damage over time.",
                    }
                    data["passives"] = [
                        {"name": "Webbed Mind", "info": "Passive one details."},
                        {"name": "", "info": "Passive two details."},
                        {"name": "", "info": ""},
                    ]
                    data_file.write_text(json.dumps(data), encoding="utf-8")
                    command_input.focus()
                    command_input.value = "class Arachnomancer"
                    await pilot.press("enter")
                    await pilot.pause()

                    await pilot.click("#nav-enhancements")
                    await pilot.pause()
                    self.assertEqual(
                        str(app.query_one("#info-session", Static).render()).strip(),
                        "Enhancements",
                    )
                    self.assertTrue(help_button.display)
                    self.assertEqual(help_button.label, "← Back")
                    self.assertTrue(home_button.display)
                    self.assertTrue(
                        app.query_one("#info-nav-separator", Static).display
                    )
                    self.assertEqual(
                        [button.label for button in app.query("#info-content Button")],
                        ["Solo", "Group", "Ultra"],
                    )
                    self.assertTrue(
                        all(
                            button.region.x == info_content.region.x
                            for button in app.query("#info-content Button")
                        )
                    )
                    await pilot.click("#nav-mode-Solo")
                    await pilot.pause()
                    self.assertEqual(
                        str(app.query_one("#info-session", Static).render()).strip(),
                        "Solo",
                    )
                    detail_buttons = list(app.query("#info-content Button"))
                    self.assertEqual(
                        [button.label for button in detail_buttons],
                        ["Class: Lucky", "Helm: Type", "Weapon: Type", "Cape: Type"],
                    )
                    detail_text = app.query_one("#detail-0-text", Static)
                    self.assertFalse(detail_text.display)
                    await pilot.click("#detail-0")
                    await pilot.pause(0.2)
                    self.assertTrue(detail_text.display)
                    self.assertEqual(
                        str(detail_text.render()), "Improves critical chance."
                    )
                    await pilot.click("#detail-0")
                    await pilot.pause(0.2)
                    self.assertFalse(detail_text.display)

                    await pilot.click("#info-back")
                    await pilot.pause(0.2)
                    self.assertEqual(
                        str(app.query_one("#info-session", Static).render()).strip(),
                        "Enhancements",
                    )
                    await pilot.click("#info-back")
                    await pilot.pause(0.2)
                    self.assertEqual(
                        str(app.query_one("#info-session", Static).render()).strip(),
                        class_name,
                    )
                    await pilot.click("#nav-skills")
                    await pilot.pause()
                    self.assertTrue(help_button.display)
                    self.assertTrue(home_button.display)
                    skill_buttons = list(app.query("#info-content Button"))
                    self.assertEqual(
                        [button.label for button in skill_buttons],
                        [
                            "Venom Strike",
                            "Skill 2",
                            "Skill 3",
                            "Skill 4",
                            "Skill 5",
                            "Webbed Mind",
                            "Passive 2",
                        ],
                    )
                    self.assertNotIn(
                        "Passive 3", [button.label for button in skill_buttons]
                    )

                    data["passives"][2] = {
                        "name": "",
                        "info": "Third passive details.",
                    }
                    data_file.write_text(json.dumps(data), encoding="utf-8")
                    command_input.focus()
                    command_input.value = "class Arachnomancer"
                    await pilot.press("enter")
                    await pilot.pause()
                    await pilot.click("#nav-skills")
                    await pilot.pause(0.2)
                    skill_buttons = list(app.query("#info-content Button"))
                    self.assertEqual(skill_buttons[-1].label, "Passive 3")
                    third_passive_id = skill_buttons[-1].id
                    await pilot.click(f"#{third_passive_id}")
                    await pilot.pause()
                    third_details = app.query_one(
                        f"#{third_passive_id}-text", Static
                    )
                    self.assertTrue(third_details.display)
                    self.assertEqual(
                        str(third_details.render()), "Third passive details."
                    )
                    await pilot.press("ctrl+c")

    async def test_class_command_works_without_a_loaded_account(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            class_directory = Path(temporary_directory) / "classes"
            app = LinuxConsoleApp(
                settings_path=Path(temporary_directory) / "config.json",
                class_data_path=class_directory,
            )
            async with app.run_test() as pilot:
                command_input = app.query_one("#command-input", Input)
                command_input.value = "/class Dragon of Time"
                await pilot.press("enter")
                await pilot.pause()

                self.assertEqual(
                    str(app.query_one("#info-session", Static).render()).strip(),
                    "Dragon of Time",
                )
                self.assertEqual(
                    [button.label for button in app.query("#info-content Button")],
                    ["Enhancements", "Skills"],
                )
                self.assertTrue(
                    class_data_path("Dragon of Time", class_directory).exists()
                )
                command_input = app.query_one("#command-input", Input)
                command_input.value = "/not-a-command"
                await pilot.press("enter")
                await pilot.pause()

                self.assertEqual(
                    str(app.query_one("#info-session", Static).render()).strip(),
                    "Dragon of Time",
                )
                self.assertEqual(
                    [button.label for button in app.query("#info-content Button")],
                    ["Enhancements", "Skills"],
                )

    async def test_info_shows_commands_without_a_saved_account(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            app = LinuxConsoleApp(
                settings_path=Path(temporary_directory) / "config.json",
                class_data_path=Path(temporary_directory) / "classes",
            )
            async with app.run_test() as pilot:
                labels = [
                    str(widget.render())
                    for widget in app.query("#info-content Static")
                ]
                self.assertNotIn("Commands", labels)
                self.assertFalse(any("Loaded" in label for label in labels))
                self.assertEqual(
                    str(app.query_one("#info-session", Static).render()).strip(),
                    "Commands",
                )
                command_input = app.query_one("#command-input", Input)
                command_input.focus()
                command_input.value = "/char "
                await pilot.pause()
                await pilot.press("tab")
                await pilot.pause()
                self.assertEqual(command_input.value, "/char CHAR ")

                self.assertIn(
                    "/update",
                    " ".join(
                        str(widget.render())
                        for widget in app.query("#info-content Static")
                    ),
                )
                command_names = [
                    str(widget.render()).split(maxsplit=1)[0]
                    for widget in app.query("#info-content Static")
                ]
                self.assertEqual(
                    command_names,
                    ["/char", "/reload", "/class", "/return", "/update"],
                )
                command_input.focus()
                command_input.value = "/update"
                await pilot.press("enter")
                await pilot.pause()
                self.assertEqual(
                    [
                        app.query_one("#update-yes", Button).label,
                        app.query_one("#update-no", Button).label,
                    ],
                    ["YES", "NO"],
                )
                self.assertIn(
                    "Synchronize your information",
                    str(app.query_one(".update-warning", Static).render()),
                )
                await pilot.click("#update-no")
                await pilot.pause()
                self.assertEqual(
                    str(app.query_one("#info-session", Static).render()).strip(),
                    "Commands",
                )

                command_input.focus()
                command_input.value = "/update"
                await pilot.press("enter")
                await pilot.pause()
                self.assertEqual(
                    [
                        app.query_one("#update-yes", Button).label,
                        app.query_one("#update-no", Button).label,
                    ],
                    ["YES", "NO"],
                )
                await pilot.click("#update-yes")
                await pilot.pause()
                self.assertIn(
                    "not configured yet",
                    str(app.query_one(".update-warning", Static).render()),
                )
                await pilot.click("#update-ok")
                await pilot.pause()
                self.assertEqual(
                    str(app.query_one("#info-session", Static).render()).strip(),
                    "Commands",
                )

                command_input.focus()
                command_input.value = "/char"
                await pilot.press("enter")
                await pilot.pause()
                self.assertEqual(
                    str(app.query_one("#info-session", Static).render()).strip(),
                    "Saved Characters",
                )
                self.assertIn(
                    "No saved characters",
                    " ".join(
                        str(widget.render())
                        for widget in app.query("#info-content Static")
                    ),
                )

    async def test_saved_account_refreshes_when_app_opens(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            settings_path = temporary_path / "config.json"
            settings_path.write_text('{"account":"Potato Lady"}', encoding="utf-8")
            with patch(
                "linux_console.app.fetch_classes", return_value=["Arachnomancer"]
            ) as fetch:
                app = LinuxConsoleApp(
                    settings_path=settings_path,
                    class_data_path=temporary_path / "classes",
                )
                async with app.run_test():
                    await asyncio.sleep(0.1)
                    fetch.assert_called_once_with("Potato Lady")
                    class_list = app.query_one("#class-list", ListView)
                    self.assertEqual(
                        [
                            str(item.query_one(Static).render())
                            for item in class_list.children
                        ],
                        ["Arachnomancer"],
                    )
                    self.assertIn(
                        "Commands",
                        str(app.query_one("#info-session", Static).render()),
                    )
