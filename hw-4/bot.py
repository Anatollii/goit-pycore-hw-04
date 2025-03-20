def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    """Додаємо новий контакт"""
    if len(args) < 2:
        return "Помилка: введіть ім'я та номер телефону!"
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} добавлен."


def change_contact(args, contacts):
    """Зміняємо контакт"""
    if len(args) < 2:
        return "Помилка: введіть ім'я та номер!"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Контакт {name} оновлений."
    return "Помилка: контакт не знайдено."


def show_phone(args, contacts):
    """Номер телефону за ім'ям"""
    if len(args) < 1:
        return "Помилка: введіть ім'я контакта!"
    name = args[0]
    return contacts.get(name, "Помилка: контакт не знайден.")


def show_all(contacts):
    """Виводимо всі контакти"""
    if not contacts:
        return "Контактів поки немає."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}  # Словник контактів
    print("📞 Ласкаво просимо в помічник-бота!")

    while True:
        user_input = input("Введіть команду: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("👋 До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Помилка: невідома команда!")


if __name__ == "__main__":
    main()
