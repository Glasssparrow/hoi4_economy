from os import path, listdir
from constants import PATH_TO_PROVINCES, GAME_DATA_FILE_TYPE


def create_tags_file():
    provinces_dict = {}  # Словарь с итоговыми данными
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
        full_file_name = path.basename(file)  # Имя файла вместе с расширением
        file_name = full_file_name[
                    :-len(full_file_name.split(".")[-1]) - 1  # -1 для удаления точки
                    ]  # Имя файла
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
        for line in raw_list:
            if "add_core_of" in line:
                core = line.split("=")[1]
                if "#" in core:
                    core = core.split("#")[0]
                core = core.strip()
                if core not in tags:
                    tags.append(core)
    return tags