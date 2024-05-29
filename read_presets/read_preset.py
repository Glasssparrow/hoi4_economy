from os import path, listdir
from simulation_code.create_a_country import get_data, get_country
from simulation_code.events import Event
from constants_and_settings.constants import PRESETS_FOLDER


def read_preset(preset_name):
    # Проверяем наличие файла с именем preset_name
    files_type = ".txt"
    raw_list = listdir(PRESETS_FOLDER)
    files_names = []
    for file in raw_list:
        if file[-len(files_type):] == files_type:
            files_names.append(file[:-len(files_type)])
    if preset_name not in files_names:
        raise Exception(f"Файл {preset_name}.txt не найден")

    # Читаем файл
    path_to_preset = path.join(PRESETS_FOLDER, preset_name+files_type)
    with open(path_to_preset, encoding="utf8") as link_to_the_file:
        preset = link_to_the_file.read()
    # Преобразуем строку в лист приказов
    splitted_string = preset.split("\n")
    orders = []
    for line in splitted_string:
        edited_line = line.strip()
        if "#" in edited_line:  # Убираем комментарии
            edited_line = edited_line.split("#")[0]
            edited_line = edited_line.strip()
        if edited_line:  # Все не пустые строки в приказы
            orders.append(edited_line)
    return orders


def turn_preset_into_country(orders):
    # Преобразуем лист приказов в экземпляр Country
    with open("tags.txt", "r") as json_file:
        all_tags = json_file.read()  # Список кодов стран
    data = get_data()                # Данные по регионам
    if orders[0].upper() not in all_tags:
        by_tag = False
    else:
        by_tag = True
    # Формирование экземпляра.
    name_or_tag = orders.pop(0)
    country = get_country(data=data, name_or_tag=name_or_tag, by_tag=by_tag)
    for order in orders:
        country.add_event(Event(order))
    return country
