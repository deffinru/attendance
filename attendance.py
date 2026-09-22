"""Модуль учёта посещений."""
import csv
from datetime import date, datetime


def check_in(name: str, filename: str = "attendance.csv") -> None:
    """Зарегистрировать вход сотрудника."""
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, "in", datetime.now().isoformat()])

def check_out(name: str, filename: str = "attendance.csv") -> None:
    """Зарегистрировать выход сотрудника."""
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, "out", datetime.now().isoformat()])


if __name__ == "__main__":
    name = input("Введите имя: ")
    check_in(name)
    print("Вход зарегистрирован.")