from os import path, listdir
from simulation_code.create_a_country import get_data, get_country
from simulation_code.events import Event


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
simulations_instructions = []  # Список листов с приказами
for string in raw_strings:
    splitted_string = string.split("\n")
    orders_list = []
    for line in splitted_string:
        edited_line = line.strip()
        if "#" in edited_line:  # Убираем комментарии
            edited_line = edited_line.split("#")[0]
            edited_line = edited_line.strip()
        if edited_line:  # Все не пустые строки в приказы
            orders_list.append(edited_line)
    simulations_instructions.append(orders_list)

# Необходимые для расчета данные
with open("tags.txt", "r") as json_file:
    all_tags = json_file.read()
data = get_data()

results = []  # Для итоговых экземпляров стран
for orders in simulations_instructions:
    if orders[0].upper() not in all_tags:
        by_tag = False
    else:
        by_tag = True
    # Оставляем только ивенты в списке приказов,
    # а также передаем название/тэг в переменную.
    name_or_tag = orders.pop(0)
    country = get_country(data=data, name_or_tag=name_or_tag, by_tag=by_tag)
    results.append(country)
    for order in orders:
        country.add_event(Event(order))
    for x in range(730):
        country.calculate_day(x)

for country in results:
    pass
