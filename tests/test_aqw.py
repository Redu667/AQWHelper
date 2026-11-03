import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

from linux_console.aqw import (
    fetch_classes,
    load_account_history,
    load_default_account,
    remove_saved_account,
    save_default_account,
)


class FetchClassesTests(unittest.TestCase):
    def test_reads_inventory_classes_and_strips_rank_suffix(self) -> None:
        page = "<script>var ccid = 12345;</script>"
        inventory = json.dumps(
            [
                {"strType": "Class", "strName": "Arachnomancer (Rank 10)"},
                {"strType": "Item", "strName": "Potion"},
                {"strType": "Class", "strName": "Arcana Invoker"},
                {"strType": "Class", "strName": "Arachnomancer (Rank 10)"},
            ]
        )
        with patch(
            "linux_console.aqw._fetch_text", side_effect=[page, inventory]
        ) as fetch:
            self.assertEqual(
                fetch_classes("Potato Lady"), ["Arachnomancer", "Arcana Invoker"]
            )

        page_url = urlparse(fetch.call_args_list[0].args[0])
        self.assertEqual(parse_qs(page_url.query), {"id": ["Potato Lady"]})
        inventory_url = urlparse(fetch.call_args_list[1].args[0])
        self.assertEqual(parse_qs(inventory_url.query), {"ccid": ["12345"]})

    def test_fails_when_character_page_has_no_character_id(self) -> None:
        with patch("linux_console.aqw._fetch_text", return_value="<html></html>"):
            with self.assertRaisesRegex(ValueError, "No character ID"):
                fetch_classes("Unknown Character")

    def test_rejects_empty_account_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "Enter an AQW character name"):
            fetch_classes("  ")

    def test_saves_and_loads_character_history(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            config_path = Path(temporary_directory) / "config.json"
            save_default_account(config_path, "Potato Lady")
            save_default_account(config_path, "Another Character")
            save_default_account(config_path, "potato lady")

            self.assertEqual(
                load_account_history(config_path),
                ["Another Character", "potato lady"],
            )
            config = json.loads(config_path.read_text(encoding="utf-8"))
            self.assertEqual(config["account"], "potato lady")

    def test_removes_character_and_clears_matching_default(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            config_path = Path(temporary_directory) / "config.json"
            save_default_account(config_path, "Older Character")
            save_default_account(config_path, "Latest Character")

            self.assertTrue(remove_saved_account(config_path, "latest character"))
            self.assertEqual(load_account_history(config_path), ["Older Character"])
            self.assertIsNone(load_default_account(config_path))
            self.assertFalse(remove_saved_account(config_path, "Missing Character"))
