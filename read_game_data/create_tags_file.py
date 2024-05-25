from os import path, listdir
from constants_and_settings.constants import PATH_TO_PROVINCES, GAME_DATA_FILE_TYPE


def create_tags_file():
    files_list = listdir(PATH_TO_PROVINCES)  # Список путей к файлам
    provinces_list = []  # Список путей к текстовым файлам
    # Заполняем список путей к текстовым файлам
    for file in files_list:
        if file[-len(GAME_DATA_FILE_TYPE):] == GAME_DATA_FILE_TYPE:
            provinces_list.append(path.join(PATH_TO_PROVINCES, file))
    # Лист с уникальными кодами стран
    tags = []
    # Цикл заполнения словаря с итоговыми данными
    for file in provinces_list:
        with open(file) as link_to_the_file:  # Читаем данные
            raw_string = link_to_the_file.read()  # Получаем сырую строку данных
        raw_list = raw_string.split("\n")  # Делим текст по строкам
        # Удаляем пустые строки
        for element_number in reversed(range(len(raw_list))):
            if not raw_list[element_number]:
                raw_list.pop(element_number)
        for line in raw_list:
            if "add_core_of" in line:
                core = line.split("=")[1]
                if "#" in core:
                    core = core.split("#")[0]
                core = core.strip()
                if core not in tags:
                    tags.append(core)
    return tags
