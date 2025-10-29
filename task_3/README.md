# Завдання 3 (не обов'язкове): Аналіз файлів логів

## Опис завдання

Розробка Python-скрипту для аналізу файлів логів. Скрипт читає лог-файл, підраховує статистику за рівнями логування (INFO, ERROR, DEBUG, WARNING) та може фільтрувати записи за конкретним рівнем.

## Ключові концепції

### 1. **Аргументи командного рядка (sys.argv)**
Скрипт приймає шлях до файлу та опціональний рівень логування як аргументи.

### 2. **Робота з файлами (Path, open)**
Використання `pathlib.Path` для роботи зі шляхами та безпечне читання файлів.

### 3. **Обробка помилок (try/except)**
Коректна обробка відсутніх файлів та помилок читання.

### 4. **Функціональне програмування**
- `filter()` з lambda для фільтрації логів за рівнем
- `map()` для отримання рівнів логування
- Лямбда-функції для компактного коду

## Реалізовані функції

### 1. `parse_log_line(line: str) -> dict`
Парсить рядок логу та повертає словник з компонентами:
```python
{
    'date': '2024-01-22',
    'time': '08:30:01',
    'level': 'INFO',
    'message': 'User logged in successfully.'
}
```

### 2. `load_logs(file_path: str) -> list`
Завантажує логи з файлу та парсить кожен рядок.

### 3. `filter_logs_by_level(logs: list, level: str) -> list`
Фільтрує логи за рівнем використовуючи `filter()` та lambda:
```python
filter(lambda log: log.get('level', '').upper() == level.upper(), logs)
```

### 4. `count_logs_by_level(logs: list) -> dict`
Підраховує кількість записів для кожного рівня використовуючи `map()`.

### 5. `display_log_counts(counts: dict)`
Виводить статистику у вигляді таблиці.

### 6. `display_filtered_logs(logs: list, level: str)`
Виводить детальну інформацію для відфільтрованих логів.

## Формат лог-файлу

```
YYYY-MM-DD HH:MM:SS LEVEL Message text
```

Приклад:
```
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 09:00:45 ERROR Database connection failed.
```

## Запуск

### 1. Тільки статистика:
```bash
cd task_3
python task_3.py logfile.log
```

### 2. Статистика + фільтрація за рівнем:
```bash
python task_3.py logfile.log error
python task_3.py logfile.log info
python task_3.py logfile.log debug
python task_3.py logfile.log warning
```

## Приклади використання

### Приклад 1: Загальна статистика

```bash
python task_3.py logfile.log
```

**Вивід:**
```
📂 Завантаження логів з файлу: logfile.log
✅ Завантажено 10 записів

Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
WARNING          | 1
ERROR            | 2
```

### Приклад 2: Фільтрація за рівнем ERROR

```bash
python task_3.py logfile.log error
```

**Вивід:**
```
📂 Завантаження логів з файлу: logfile.log
✅ Завантажено 10 записів

Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
WARNING          | 1
ERROR            | 2

Деталі логів для рівня 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

## Обробка помилок

### Файл не знайдено:
```bash
python task_3.py nonexistent.log
```
```
❌ Помилка: Файл 'nonexistent.log' не знайдено
```

### Не вказано файл:
```bash
python task_3.py
```
```
❌ Помилка: Не вказано шлях до файлу логів

Використання:
  python task_3.py <шлях_до_файлу_логів> [рівень_логування]

Приклад:
  python task_3.py logfile.log
  python task_3.py logfile.log error
```

## Функціональне програмування

### 1. Використання `filter()` та `lambda`:
```python
# Фільтрація логів за рівнем
filtered = list(filter(lambda log: log['level'] == level, logs))
```

### 2. Використання `map()`:
```python
# Отримання всіх рівнів логування
levels = map(lambda log: log.get('level', 'UNKNOWN'), logs)
```

### 3. Лямбда-функції:
```python
# Компактний код без оголошення окремих функцій
lambda log: log.get('level', '').upper() == level.upper()
```

## Критерії виконання

- ✅ Скрипт приймає шлях до файлу як аргумент командного рядка
- ✅ Опціональний аргумент для фільтрації за рівнем логування
- ✅ Парсинг логів з функцією `parse_log_line()`
- ✅ Завантаження логів з функцією `load_logs()`
- ✅ Фільтрація з функцією `filter_logs_by_level()`
- ✅ Підрахунок з функцією `count_logs_by_level()`
- ✅ Форматований вивід таблиці з функцією `display_log_counts()`
- ✅ Обробка помилок (FileNotFoundError, IOError)
- ✅ Використання елементів функціонального програмування (filter, map, lambda)
- ✅ Чистий код з коментарями та документацією

## Технічні деталі

### Використані модулі:
- `sys` - робота з аргументами командного рядка
- `pathlib.Path` - робота зі шляхами файлів
- `typing` - type hints для кращої читабельності

### Type Hints:
- `parse_log_line(line: str) -> Dict[str, str]`
- `load_logs(file_path: str) -> List[Dict[str, str]]`
- `filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]`
- `count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]`

## Тестовий файл

В папці task_3 є файл `logfile.log` з прикладами логів для тестування.

