# Attendance — учёт посещений

Простой Python-скрипт для учёта посещений с сохранением в CSV.

## Использование

python attendance.py

## Формат данных

См. attendance.csv.example.

## Функции

### check_in(name, filename)

Регистрирует вход сотрудника. Записывает в CSV строку:

name,event,datetime

Пример:

python attendance.py