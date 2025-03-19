def get_cats_info(path):
    cats_list = []


    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",") # Розділяємо рядок по комі

                if len(data) == 3: # Перевірка на те що у рядку 3 елемента
                    cat_dict = {"id": data[0], "name": data[1], "age": data[2]}
                    cats_list.append(cat_dict)
                else:
                    print(f"Помилка формату рядка {line}")
    except FileNotFoundError:
        print("Файл не знайдено, перевірте шлях")
    except Exception as e:
        print("Помилка: {e}")
    return cats_list

# Тестуємо
file_path = "cats_file.txt"
cats_info = get_cats_info(file_path)
print(cats_info)

