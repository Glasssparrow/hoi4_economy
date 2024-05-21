from os import path, listdir
from ast import literal_eval
from json import dump


PATH = "provinces"
FORMATS_LIST = ".txt"


def is_text(letter):
    if letter.isalpha():
        return True
    elif letter == "_":
        return True
    else:
        return False


# noinspection PyTypeChecker
def add_quotes(string, maximum_phrases=20):
    """Добавляем кавычки тексту, чтобы python распознавал его."""
    # Исправляем названия dlc
    string = string.replace(
        "Arms Against Tyranny",
        "Arms_Against_Tyranny",
    )
    text = []
    for x in range(maximum_phrases):
        text.append([None, None])
    # Находим фразы
    for x in range(len(string)-1):
        # Избегание кавычек нужно для того,
        # чтобы оставить название с номером.
        if (
            (not is_text(string[x]) and not string[x].isdigit())
            and is_text(string[x+1])
            and string[x] != '"' and string[x+1] != '"'
        ):
            for y in range(maximum_phrases):
                if not text[y][0] is None:
                    continue
                text[y][0] = x+1
                break
        if (
            is_text(string[x]) and
            (not is_text(string[x+1]) and not string[x+1].isdigit())
            and string[x] != '"' and string[x+1] != '"'
        ):
            for y in range(maximum_phrases):
                if text[y][1]:
                    continue
                text[y][1] = x+1
                break
    # Берем в кавычки полностью найденные фразы.
    for phrase in reversed(text):
        if phrase[0] and phrase[1]:
            string = (
                    string[:phrase[0]] + '"' +
                    string[phrase[0]:phrase[1]] + '"' +
                    string[phrase[1]:]
            )
    return string


def separate_numbers(string, max_spaces=6):
    """Разделяем числа запятыми. А также число строка, тоже.
    Превращаем даты в мессиво."""
    for x in range(len(string)-2):
        if (
            string[x].isdigit() and
            string[x+1] == " " and
            string[x+2].isalpha()
        ):
            string = string[:x+1] + "," + string[x+2:]
        # Табуляцию тоже убираем
        if (
            string[x].isdigit() and
            string[x+1] == "\t" and
            string[x+2].isdigit()
        ):
            string = string[:x+1] + "," + string[x+2:]
    for y in range(max_spaces):
        for x in range(len(string) - 2 - y):
            if (
                string[x].isdigit() and
                string[x+1:x+y+2] == " "*(y+1) and
                string[x+2+y].isdigit()
            ):
                string = string[:x+1] + "," + " "*y + string[x+2:]
    return string


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
    file_name = full_file_name.split(".")[0]  # Имя файла
    province_number = int(file_name.split("-")[0])  # Номер провинции по порядку
    province_name = file_name.split("-")[1].lower()  # Название провинции

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
    # Судя по всему число в начале это дата, или что-то подобное.
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

    # Преобразуем в python код
    for old_line in raw_list:
        if "#" in old_line:
            line = old_line.split("#")[0]  # Удаляем комментарии
        else:
            line = old_line
        # Заменяем "=" на ":" т.к. преобразовываем в словарь
        new_line = line.replace("=", ":")
        # Запятые в конце строки
        if (
            ":" in new_line and
            new_line[-1] != ":" and
            not ("{" in new_line and "}" not in new_line)
            or "}" in new_line
        ):
            new_line = new_line + ","
        new_line = separate_numbers(new_line)  # Разделяем числа запятыми
        new_line = add_quotes(new_line)  # Добавляем свои кавычки
        new_list.append(new_line)  # Для итогового листа
    # Собираем итоговый текст
    new_text = ""
    for line in new_list:
        new_text = f"{new_text}{line}\n"
    data_dict = literal_eval(new_text)[0]

    # Теперь можно начать заполнять наш словарь
    provinces_dict[province_number] = {}  # Добавляем словарь для данных провинции
    # Для удобства берем ссылки на словарь истории и словарь провинции
    prov = provinces_dict[province_number]
    history = data_dict.get("history", {})
    # Читаем данные
    prov["name"] = province_name  # Добавляем имя
    prov["owner"] = history["owner"]
    prov["infrastructure"] = history.get("infrastructure", 0)
    prov["factories"] = history.get("industrial_complex", 0)
    prov["military_factories"] = history.get("arms_factory", 0)
    prov["shipyards"] = history.get("dockyard", 0)
    prov["fuel_silo"] = history.get("fuel_silo", 0)
    prov["anti_air"] = history.get("anti_air_building", 0)
    prov["air_base"] = history.get("air_base", 0)
    prov["radar"] = history.get("radar_station", 0)
    prov["synth_oil"] = history.get("synthetic_refinery", 0)
    # Список типов регионов с максимумами слотов
    lands = {
        "wasteland": 0,
        "enclave": 0,
        "tiny_island": 0,
        "pastoral": 1,
        "small_island": 1,
        "rural": 2,
        "town": 4,
        "large_town": 5,
        "city": 6,
        "large_city": 8,
        "metropolis": 10,
        "megalopolis": 12,
    }
    for k, v in lands.items():  # Устанавливаем максимум слотов
        if data_dict["state_category"] == k:
            prov["max_factories"] = v


with open("provinces.txt", "w") as json_file:
    dump(provinces_dict, json_file)
