"""
Завдання 3 (не обов'язкове)
---------------------------
Опис: Аналіз файлів логів з підрахунком статистики за рівнями логування
      та можливістю фільтрації за конкретним рівнем.

Тема: Функціональне програмування та вбудовані модулі Python
Концепції: Робота з файлами, Аргументи командного рядка, Обробка помилок,
          Функціональне програмування (filter, lambda)
"""

import sys
from typing import Dict, List
from pathlib import Path


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Парсить рядок логу та повертає словник з компонентами.
    
    Формат рядка: "YYYY-MM-DD HH:MM:SS LEVEL Message text"
    
    Args:
        line (str): Рядок з логу
        
    Returns:
        dict: Словник з ключами 'date', 'time', 'level', 'message'
        
    Example:
        >>> parse_log_line("2024-01-22 08:30:01 INFO User logged in")
        {'date': '2024-01-22', 'time': '08:30:01', 'level': 'INFO', 
         'message': 'User logged in'}
    """
    try:
        # Розділяємо рядок на частини
        parts = line.strip().split(' ', 3)
        
        if len(parts) < 4:
            # Якщо рядок не відповідає очікуваному формату
            return {}
        
        return {
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'message': parts[3]
        }
    except Exception as e:
        print(f"Помилка парсингу рядка: {e}")
        return {}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Завантажує логи з файлу та парсить кожен рядок.
    
    Args:
        file_path (str): Шлях до файлу логів
        
    Returns:
        list: Список словників з розпарсеними логами
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено
        IOError: Якщо виникла помилка при читанні файлу
    """
    logs = []
    
    try:
        # Використовуємо Path для кращої роботи зі шляхами
        log_file = Path(file_path)
        
        if not log_file.exists():
            raise FileNotFoundError(f"Файл '{file_path}' не знайдено")
        
        # Читаємо файл та парсимо кожен рядок
        with log_file.open('r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # Пропускаємо порожні рядки
                    parsed_log = parse_log_line(line)
                    if parsed_log:  # Додаємо тільки успішно розпарсені рядки
                        logs.append(parsed_log)
        
        return logs
        
    except FileNotFoundError as e:
        print(f"❌ Помилка: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"❌ Помилка читання файлу: {e}")
        sys.exit(1)


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Фільтрує логи за вказаним рівнем логування.
    
    Використовує функціональний підхід з filter та lambda.
    
    Args:
        logs (list): Список логів
        level (str): Рівень логування для фільтрації (INFO, ERROR, DEBUG, WARNING)
        
    Returns:
        list: Відфільтрований список логів
    """
    # Функціональне програмування: використання filter та lambda
    return list(filter(lambda log: log.get('level', '').upper() == level.upper(), logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    
    Args:
        logs (list): Список логів
        
    Returns:
        dict: Словник з кількістю записів для кожного рівня
    """
    counts = {}
    
    # Функціональне програмування: використання map для отримання рівнів
    levels = map(lambda log: log.get('level', 'UNKNOWN'), logs)
    
    # Підраховуємо кількість для кожного рівня
    for level in levels:
        counts[level] = counts.get(level, 0) + 1
    
    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Виводить статистику логів у вигляді таблиці.
    
    Args:
        counts (dict): Словник з кількістю записів для кожного рівня
    """
    print("\nРівень логування | Кількість")
    print("-" * 17 + "|" + "-" * 10)
    
    # Сортуємо за рівнем логування для красивого виводу
    # Порядок: INFO, DEBUG, WARNING, ERROR, інші
    order = ['INFO', 'DEBUG', 'WARNING', 'ERROR']
    
    # Спочатку виводимо відомі рівні в заданому порядку
    for level in order:
        if level in counts:
            print(f"{level:<17}| {counts[level]}")
    
    # Потім виводимо інші рівні, якщо вони є
    for level, count in sorted(counts.items()):
        if level not in order:
            print(f"{level:<17}| {count}")


def display_filtered_logs(logs: List[Dict[str, str]], level: str) -> None:
    """
    Виводить деталі логів для вказаного рівня.
    
    Args:
        logs (list): Список відфільтрованих логів
        level (str): Рівень логування
    """
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    
    if not logs:
        print(f"  Записів з рівнем '{level.upper()}' не знайдено.")
        return
    
    for log in logs:
        # Форматуємо вивід: дата час - повідомлення
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    """
    Головна функція для аналізу файлів логів.
    """
    # Перевірка аргументів командного рядка
    if len(sys.argv) < 2:
        print("❌ Помилка: Не вказано шлях до файлу логів")
        print("\nВикористання:")
        print(f"  python {sys.argv[0]} <шлях_до_файлу_логів> [рівень_логування]")
        print("\nПриклад:")
        print(f"  python {sys.argv[0]} logfile.log")
        print(f"  python {sys.argv[0]} logfile.log error")
        sys.exit(1)
    
    # Отримуємо шлях до файлу
    log_file_path = sys.argv[1]
    
    # Отримуємо опціональний рівень логування для фільтрації
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"📂 Завантаження логів з файлу: {log_file_path}")
    
    # Завантажуємо логи
    logs = load_logs(log_file_path)
    
    if not logs:
        print("⚠️  Файл логів порожній або не містить валідних записів")
        sys.exit(0)
    
    print(f"✅ Завантажено {len(logs)} записів")
    
    # Підраховуємо статистику
    log_counts = count_logs_by_level(logs)
    
    # Виводимо загальну статистику
    display_log_counts(log_counts)
    
    # Якщо вказано рівень для фільтрації, виводимо деталі
    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        display_filtered_logs(filtered_logs, filter_level)


if __name__ == "__main__":
    main()

