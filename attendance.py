"""Модуль учёта посещений."""
import csv
from datetime import date


def add_visit(name: str, filename: str = "attendance.csv") -> None:
    """Добавить запись о посещении."""
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, date.today().isoformat()])


if __name__ == "__main__":
    name = input("Введите имя: ")
    add_visit(name)
    print("Запись добавлена.")