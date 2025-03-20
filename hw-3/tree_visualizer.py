import os
import sys
from colorama import init, Fore

init(autoreset=True)

def show_tree(directory, level=0):
    try:
        items = sorted(os.listdir(directory))
        for item in items:
            path = os.path.join(directory, item)
            indent = "  " * (level * 4)

            if os.path.isdir(path):
                print(Fore.BLUE + f"{indent}📂{item}")
                show_tree(path, level + 1)

            else:
                print(Fore.GREEN + f"{indent}  {item}")
    except PermissionError:
        print(Fore.RED + f"{indent} ⛔ Немає доступу")

if len(sys.argv) < 2:
    print(Fore.RED + "Помилка, вкажіть шлях дерикторії")
    sys.exit(1)

directory_path = sys.argv[1]

if not os.path.exists(directory_path):
    print(Fore.RED + f"Помилка, дерикторія {directory_path} не знайдена")
    sys.exit(1)

print(Fore.YELLOW + f"\n📁 Структура дерикторії: {directory_path}\n")
show_tree(directory_path)


