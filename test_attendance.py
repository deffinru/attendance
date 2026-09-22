"""Тесты для модуля attendance."""
import os
import unittest

from attendance import check_in, check_out
from attendance import calculate_duration



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

class TestCalculateDuration(unittest.TestCase):
    def setUp(self):
        self.filename = "test_attendance.csv"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_duration_between_in_and_out(self):
        """Проверяем расчёт длительности между входом и выходом."""
        check_in("Иван", self.filename)
        check_out("Иван", self.filename)
        duration = calculate_duration("Иван", self.filename)
        self.assertIsInstance(duration, float)
        self.assertGreaterEqual(duration, 0)


if __name__ == "__main__":
    unittest.main()