import json
import tempfile
import unittest
from pathlib import Path

from linux_console.class_data import (
    ENHANCEMENT_MODES,
    ENHANCEMENT_SLOTS,
    class_data_path,
    load_or_create_class_data,
)


class ClassDataTests(unittest.TestCase):
    def test_shared_template_matches_generated_class_template(self) -> None:
        template_path = (
            Path(__file__).resolve().parents[1] / "templates" / "template.json"
        )
        shared_template = json.loads(template_path.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as temporary_directory:
            generated_template, _ = load_or_create_class_data(
                "template", Path(temporary_directory)
            )

        self.assertEqual(shared_template, generated_template)

    def test_creates_editable_template_for_missing_class(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            data, path = load_or_create_class_data("Dragon of Time", directory)

            self.assertEqual(path, class_data_path("Dragon of Time", directory))
            self.assertTrue(path.is_file())
            self.assertEqual(data["class_name"], "Dragon of Time")
            self.assertEqual(set(data["enhancements"]), set(ENHANCEMENT_MODES))
            for mode in ENHANCEMENT_MODES:
                self.assertEqual(
                    set(data["enhancements"][mode]), set(ENHANCEMENT_SLOTS)
                )
                self.assertTrue(
                    all(
                        field == {"type": "Type", "info": ""}
                        for field in data["enhancements"][mode].values()
                    )
                )
            self.assertEqual(
                data["skills"],
                [{"name": "", "info": ""} for _ in range(5)],
            )
            self.assertEqual(
                data["passives"],
                [{"name": "", "info": ""} for _ in range(2)],
            )

    def test_reads_user_edits(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            _, path = load_or_create_class_data("Arachnomancer", directory)
            data = json.loads(path.read_text(encoding="utf-8"))
            data["enhancements"]["Solo"]["Class"] = {
                "type": "Lucky",
                "info": "Increases critical chance.",
            }
            data["skills"][0] = {
                "name": "Venom Strike",
                "info": "A test skill description.",
            }
            path.write_text(json.dumps(data), encoding="utf-8")

            loaded, loaded_path = load_or_create_class_data(
                "Arachnomancer", directory
            )

            self.assertEqual(loaded_path, path)
            self.assertEqual(
                loaded["enhancements"]["Solo"]["Class"]["type"], "Lucky"
            )
            self.assertEqual(loaded["skills"][0]["name"], "Venom Strike")

    def test_reads_three_passives_and_migrates_old_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            data, path = load_or_create_class_data("Arachnomancer", directory)
            data.pop("passives")
            data["skills"][0]["name"] = "Skill 1"
            path.write_text(json.dumps(data), encoding="utf-8")

            loaded, _ = load_or_create_class_data("Arachnomancer", directory)

            self.assertEqual(loaded["skills"][0]["name"], "")
            self.assertEqual(len(loaded["passives"]), 2)
            self.assertEqual(len(json.loads(path.read_text())["passives"]), 2)

            loaded["passives"].append({"name": "Third Passive", "info": "Details."})
            path.write_text(json.dumps(loaded), encoding="utf-8")
            with_third, _ = load_or_create_class_data("Arachnomancer", directory)
            self.assertEqual(len(with_third["passives"]), 3)
            self.assertEqual(with_third["passives"][2]["name"], "Third Passive")

    def test_rejects_malformed_class_data(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            _, path = load_or_create_class_data("Arachnomancer", directory)
            path.write_text("{", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "Invalid JSON"):
                load_or_create_class_data("Arachnomancer", directory)
