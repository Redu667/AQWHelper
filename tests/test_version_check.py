import unittest
from io import BytesIO
from unittest.mock import patch

from linux_console.version_check import REMOTE_VERSION_URL, update_available


class UpdateCheckTests(unittest.TestCase):
    def test_compares_local_version_with_remote_version(self) -> None:
        with patch(
            "linux_console.version_check.urlopen",
            return_value=BytesIO(b"1.0"),
        ) as urlopen:
            self.assertFalse(update_available())
        request = urlopen.call_args.args[0]
        self.assertEqual(request.full_url, REMOTE_VERSION_URL)
        self.assertEqual(request.get_header("Cache-control"), "no-cache")
        self.assertEqual(request.get_header("Pragma"), "no-cache")
        urlopen.assert_called_once_with(request, timeout=3.0)

        with patch(
            "linux_console.version_check.urlopen",
            return_value=BytesIO(b"1.1"),
        ):
            self.assertTrue(update_available())

    def test_rejects_invalid_remote_version(self) -> None:
        with patch(
            "linux_console.version_check.urlopen",
            return_value=BytesIO(b"<html>not a version</html>"),
        ):
            with self.assertRaises(ValueError):
                update_available()
