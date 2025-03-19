def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            salaries = []

            for line in file:
                try:
                    name, salary = line.strip().split(',')  # Розділяємо рядок за комою
                    salaries.append(int(salary))  # Додаємо зарплату як число
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()}")

            if not salaries:
                return (0, 0)  # Якщо список пустий, повертаємо 0

            total = sum(salaries)
            average = total / len(salaries)

            return total, average

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None


# Приклад виклику функції
file_path = "salary_file.txt"  # Вкажіть шлях до файлу
result = total_salary(file_path)
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
