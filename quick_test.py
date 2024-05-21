from os import path, listdir
from ast import literal_eval

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
    provinces_dict[province_number] = {}  # Добавляем словарь для данных провинции
    provinces_dict[province_number]["name"] = province_name  # Добавляем имя

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
        new_list.append(new_line)
    new_text = ""
    for line in new_list:
        new_text = f"{new_text}{line}\n"
    raw_dict = literal_eval(new_text)[0]
    for k in ["history"]:
        if k not in raw_dict.keys():
            print(k, file_name)
        else:
            for y in ["owner", "buildings"]:
                if y not in raw_dict["history"].keys():
                    print(y, file_name)
