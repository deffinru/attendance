"""Тесты для модуля attendance."""
import os
import unittest

from attendance import check_in


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


if __name__ == "__main__":
    unittest.main()