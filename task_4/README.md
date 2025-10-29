# Завдання 4: Консольний бот-помічник з декораторами

## Опис завдання

Консольний бот-помічник для управління контактами з обробкою помилок за допомогою декораторів. Бот дозволяє додавати, змінювати та переглядати контакти, обробляючи всі помилки введення користувача без завершення програми.

## Ключові концепції

### 1. **Декоратори (Decorators)**
Декоратор `@input_error` обгортає функції-обробники команд і перехоплює винятки, повертаючи користувачеві зрозумілі повідомлення про помилки.

### 2. **Обробка помилок**
- `KeyError` - контакт не знайдено
- `ValueError` - недостатньо аргументів
- `IndexError` - відсутні обов'язкові аргументи
- `Exception` - загальна обробка інших помилок

### 3. **Командний інтерфейс**
Інтерактивний цикл для взаємодії з користувачем через консоль.

## Декоратор input_error

```python
def input_error(func: Callable) -> Callable:
    """
    Декоратор для обробки помилок введення користувача.
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
```

## Доступні команди

### 1. `hello`
Привітання з ботом.
```
💬 Enter a command: hello
👋 How can I help you?
```

### 2. `add [name] [phone]`
Додати новий контакт.
```
💬 Enter a command: add John 0501234567
✅ Contact added: John - 0501234567
```

### 3. `change [name] [phone]`
Змінити телефон контакту.
```
💬 Enter a command: change John 0509876543
✅ Contact updated: John - 0501234567 → 0509876543
```

### 4. `phone [name]`
Показати телефон контакту.
```
💬 Enter a command: phone John
📞 John: 0509876543
```

### 5. `all`
Показати всі контакти.
```
💬 Enter a command: all
📋 All contacts:
------------------------------
  John: 0509876543
  Alice: 0631112233
```

### 6. `close` або `exit`
Вийти з бота.
```
💬 Enter a command: exit
👋 Good bye!
```

## Обробка помилок

### Помилка 1: Недостатньо аргументів (ValueError)

```
💬 Enter a command: add
❌ Give me name and phone please.

💬 Enter a command: add Bob
❌ Give me name and phone please.
```

### Помилка 2: Контакт не знайдено (KeyError)

```
💬 Enter a command: phone Unknown
❌ Contact not found.

💬 Enter a command: change Unknown 123456
❌ Contact not found.
```

### Помилка 3: Відсутній аргумент (IndexError)

```
💬 Enter a command: phone
❌ Enter the argument for the command
```

## Запуск

```bash
cd task_4
python task_4.py
```

## Приклад діалогу

```
==================================================
🤖 Welcome to the assistant bot!
==================================================

Available commands:
  • hello          - Greet the bot
  • add [name] [phone]   - Add a new contact
  • change [name] [phone] - Change contact's phone
  • phone [name]   - Show contact's phone
  • all            - Show all contacts
  • close or exit  - Exit the bot
--------------------------------------------------

💬 Enter a command: hello
👋 How can I help you?

💬 Enter a command: add
❌ Give me name and phone please.

💬 Enter a command: add Bob
❌ Give me name and phone please.

💬 Enter a command: add Jime 0501234356
✅ Contact added: Jime - 0501234356

💬 Enter a command: add Alice 0631112233
✅ Contact added: Alice - 0631112233

💬 Enter a command: phone
❌ Enter the argument for the command

💬 Enter a command: phone Jime
📞 Jime: 0501234356

💬 Enter a command: phone Unknown
❌ Contact not found.

💬 Enter a command: all
📋 All contacts:
------------------------------
  Jime: 0501234356
  Alice: 0631112233

💬 Enter a command: change Jime 0509999999
✅ Contact updated: Jime - 0501234356 → 0509999999

💬 Enter a command: change Unknown 123456
❌ Contact not found.

💬 Enter a command: all
📋 All contacts:
------------------------------
  Jime: 0509999999
  Alice: 0631112233

💬 Enter a command: exit
👋 Good bye!
```

## Реалізовані функції

### 1. `input_error(func)` - Декоратор
Обробляє всі помилки введення користувача.

### 2. `parse_input(user_input)` - Парсер
Розбиває введення на команду та аргументи.

### 3. `add_contact(args, contacts)` - Додавання
Додає новий контакт з декоратором `@input_error`.

### 4. `change_contact(args, contacts)` - Зміна
Змінює телефон існуючого контакту з декоратором `@input_error`.

### 5. `show_phone(args, contacts)` - Перегляд
Показує телефон контакту з декоратором `@input_error`.

### 6. `show_all(args, contacts)` - Список
Показує всі контакти з декоратором `@input_error`.

## Критерії виконання

- ✅ Наявність декоратора `input_error` для всіх команд
- ✅ Обробка `KeyError` - контакт не знайдено
- ✅ Обробка `ValueError` - недостатньо аргументів
- ✅ Обробка `IndexError` - відсутні аргументи
- ✅ Кожна функція має декоратор `@input_error`
- ✅ Відповідні повідомлення про помилки
- ✅ Програма не завершується при помилках
- ✅ Коректна реакція на всі команди

## Технічні деталі

### Type Hints:
- `input_error(func: Callable) -> Callable`
- `parse_input(user_input: str) -> tuple`
- `add_contact(args: List[str], contacts: Dict[str, str]) -> str`
- `change_contact(args: List[str], contacts: Dict[str, str]) -> str`
- `show_phone(args: List[str], contacts: Dict[str, str]) -> str`
- `show_all(args: List[str], contacts: Dict[str, str]) -> str`

### Структура даних:
- `contacts: Dict[str, str]` - словник для зберігання контактів (ім'я: телефон)

### Особливості реалізації:
1. **Декоратор inner функція** - зберігає сигнатуру оригінальної функції
2. **Try-except блоки** - перехоплюють різні типи помилок
3. **Інтерактивний цикл** - продовжує роботу після помилок
4. **Емодзі** - покращують UX і читабельність виводу

