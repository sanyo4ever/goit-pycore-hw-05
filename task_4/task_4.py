"""
Завдання 4
---------
Опис: Консольний бот-помічник з обробкою помилок за допомогою декораторів.

Тема: Функціональне програмування та вбудовані модулі Python
Концепції: Декоратори, Обробка помилок, Командний інтерфейс
"""

from typing import Callable, Dict, List


def input_error(func: Callable) -> Callable:
    """
    Декоратор для обробки помилок введення користувача.
    
    Обробляє винятки KeyError, ValueError, IndexError та повертає
    відповідні повідомлення користувачеві без завершення програми.
    
    Args:
        func: Функція-обробник команди
        
    Returns:
        Обгорнута функція з обробкою помилок
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "❌ Contact not found."
        except ValueError:
            return "❌ Give me name and phone please."
        except IndexError:
            return "❌ Enter the argument for the command"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    return inner


def parse_input(user_input: str) -> tuple:
    """
    Парсить введення користувача на команду та аргументи.
    
    Args:
        user_input: Рядок введення користувача
        
    Returns:
        tuple: (команда, список аргументів)
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    return command, args


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Додає новий контакт до словника контактів.
    
    Args:
        args: Список аргументів [ім'я, телефон]
        contacts: Словник контактів
        
    Returns:
        Повідомлення про успішне додавання
        
    Raises:
        ValueError: Якщо недостатньо аргументів
    """
    if len(args) < 2:
        raise ValueError("Not enough arguments")
    
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"✅ Contact added: {name} - {phone}"


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Змінює номер телефону існуючого контакту.
    
    Args:
        args: Список аргументів [ім'я, новий_телефон]
        contacts: Словник контактів
        
    Returns:
        Повідомлення про успішну зміну
        
    Raises:
        ValueError: Якщо недостатньо аргументів
        KeyError: Якщо контакт не знайдено
    """
    if len(args) < 2:
        raise ValueError("Not enough arguments")
    
    name, phone = args[0], args[1]
    
    if name not in contacts:
        raise KeyError(f"Contact '{name}' not found")
    
    old_phone = contacts[name]
    contacts[name] = phone
    return f"✅ Contact updated: {name} - {old_phone} → {phone}"


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Показує номер телефону контакту.
    
    Args:
        args: Список аргументів [ім'я]
        contacts: Словник контактів
        
    Returns:
        Номер телефону контакту
        
    Raises:
        IndexError: Якщо не вказано ім'я
        KeyError: Якщо контакт не знайдено
    """
    if len(args) == 0:
        raise IndexError("Name is required")
    
    name = args[0]
    
    if name not in contacts:
        raise KeyError(f"Contact '{name}' not found")
    
    return f"📞 {name}: {contacts[name]}"


@input_error
def show_all(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Показує всі контакти.
    
    Args:
        args: Список аргументів (не використовується)
        contacts: Словник контактів
        
    Returns:
        Список всіх контактів або повідомлення про пустий список
    """
    if not contacts:
        return "📋 No contacts saved yet."
    
    result = "📋 All contacts:\n"
    result += "-" * 30 + "\n"
    for name, phone in contacts.items():
        result += f"  {name}: {phone}\n"
    return result.strip()


def main():
    """
    Головна функція бота - запускає цикл обробки команд.
    """
    contacts = {}
    
    print("=" * 50)
    print("🤖 Welcome to the assistant bot!")
    print("=" * 50)
    print("\nAvailable commands:")
    print("  • hello          - Greet the bot")
    print("  • add [name] [phone]   - Add a new contact")
    print("  • change [name] [phone] - Change contact's phone")
    print("  • phone [name]   - Show contact's phone")
    print("  • all            - Show all contacts")
    print("  • close or exit  - Exit the bot")
    print("-" * 50)
    
    while True:
        user_input = input("\n💬 Enter a command: ").strip()
        
        if not user_input:
            continue
        
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("👋 Good bye!")
            break
        
        elif command == "hello":
            print("👋 How can I help you?")
        
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        
        elif command == "all":
            result = show_all(args, contacts)
            print(result)
        
        else:
            print("❌ Invalid command. Type 'hello', 'add', 'change', 'phone', 'all', 'close' or 'exit'.")


if __name__ == "__main__":
    main()

