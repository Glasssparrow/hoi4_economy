from os import path, listdir
from ast import literal_eval

PATH = "provinces"
FORMATS_LIST = ".txt"


def add_quotes(string):
    for x in range(len(string)):
        pass
    print("#", string)
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
    raw_list = raw_string.split("\n")  # Делим текст по строкам
    new_list = []  # Будущий итоговый лист с файлом построчно
    # Удаляем пустые строки
    for element_number in reversed(range(len(raw_list))):
        if not raw_list[element_number]:
            raw_list.pop(element_number)
    raw_list[0] = raw_list[0][6:]  # Удаляем "state="

    # Преобразуем в python код
    for old_line in raw_list:
        if "#" in old_line:
            line = old_line.split("#")[0]  # Удаляем комментарии
        else:
            line = old_line
        # Заменяем "=" на ":" т.к. преобразовываем в словарь
        new_line = line.replace("=", ":")
        # Запятые в конце строки
        if ":" in new_line:
            new_line = new_line + ","
        # Удаляем кавычки т.к. будем вставлять свои
        new_line = new_line.replace('"', "")
        new_line = add_quotes(new_line)  # Добавляем свои кавычки
        new_list.append(new_line)
    new_text = ""
    for line in new_list:
        new_text = f"{new_text}{line}\n"
    # print(new_text)

# lets_try = literal_eval("""
# {2:3}
# """)
# print(lets_try)

# print("d".isalpha())
