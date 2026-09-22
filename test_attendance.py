"""Тесты для модуля attendance."""
import os
import unittest

from attendance import check_in, check_out


class TestCheckIn(unittest.TestCase):
    def setUp(self):
        self.filename = "test_attendance.csv"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_check_in_creates_record(self):
        """Проверяем, что check_in создаёт запись."""
        check_in("Иван", self.filename)
        self.assertTrue(os.path.exists(self.filename))

class TestCheckOut(unittest.TestCase):
    def setUp(self):
        self.filename = "test_attendance.csv"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_check_out_creates_record(self):
        """Проверяем, что check_out создаёт запись."""
        check_in("Иван", self.filename)
        check_out("Иван", self.filename)
        with open(self.filename, encoding="utf-8") as f:
            content = f.read()
        self.assertIn("out", content)


if __name__ == "__main__":
    unittest.main()