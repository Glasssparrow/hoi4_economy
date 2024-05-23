from os import path, listdir
from ast import literal_eval
from json import dump

PATH = "provinces"
FORMATS_LIST = ".txt"

provinces_dict = {}  # Словарь с итоговыми данными
files_list = listdir(PATH)  # Список путей к файлам
provinces_list = []  # Список путей к текстовым файлам
# Заполняем список путей к текстовым файлам
for file in files_list:
    if file[-len(FORMATS_LIST):] == FORMATS_LIST:
        provinces_list.append(path.join(PATH, file))
# Цикл заполнения словаря с итоговыми данными
for file in provinces_list:
    full_file_name = path.basename(file)  # Имя файла вместе с расширением
    file_name = full_file_name[
                :-len(full_file_name.split(".")[-1]) - 1  # -1 для удаления точки
                ]  # Имя файла
    province_number = int(file_name.split("-")[0])  # Номер провинции по порядку
    province_name = file_name[
                    len(file_name.split("-")[0]) + 1:  # +1 для удаления "-"
                    ]  # Название провинции
    province_name = province_name.replace("-", "_")
    province_name = province_name.rstrip()  # Удаляем пробелы с краев
    province_name = province_name.lower()

    with open(file) as link_to_the_file:  # Читаем данные
        raw_string = link_to_the_file.read()  # Получаем сырую строку данных
    # Уничтожаем все даты
    for year in range(36, 51):
        for month in range(1, 13):
            raw_string = raw_string.replace(
                f"{year}.{month}.",
                "",
            )
    # Переменные начинающиеся с чисел это ересь.
    # Судя по всему число в начале это дата, или типо того.
    raw_string = raw_string.replace(
        "843.ETH_state_development_production_speed",
        "Why_variable_starts_with_a_number",
    )
    raw_string = raw_string.replace(
        "908.ETH_state_development_production_speed",
        "Another_one"
    )
    raw_list = raw_string.split("\n")  # Делим текст по строкам
    new_list = []  # Будущий итоговый лист с файлом построчно
    # Удаляем пустые строки
    for element_number in reversed(range(len(raw_list))):
        if not raw_list[element_number]:
            raw_list.pop(element_number)
    raw_list[0] = raw_list[0].split("=")[1]  # Удаляем "state="
    