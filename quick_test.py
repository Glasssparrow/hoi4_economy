from os import path, listdir


# Читаются все файлы формата ".txt".
# Файл должен содержать название страны или её тэг
# в первой не закомментированной строке.
FILES_TYPE = ".txt"
raw_list = listdir("simulation_orders")
files_list = []  # Пути ко всем файлам с инструкциями
for file in raw_list:
    if file[-len(FILES_TYPE):] == FILES_TYPE:
        files_list.append(path.join("simulation_orders", file))
raw_strings = []  # Строки данных из файлов с инструкциями
for file in files_list:
    with open(file) as link_to_the_file:
        raw_strings.append(link_to_the_file.read())
orders_lists = []  # Список листов с приказами
for string in raw_strings:
    splitted_string = string.split("\n")
    orders = []
    for line in splitted_string:
        edited_line = line.strip()
        if "#" in edited_line:  # Убираем комментарии
            edited_line = edited_line.split("#")[0]
            edited_line = edited_line.strip()
        if edited_line:  # Все не пустые строки в приказы
            orders.append(edited_line)
    orders_lists.append(orders)
