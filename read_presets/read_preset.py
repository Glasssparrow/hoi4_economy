from os import path, listdir


def read_preset(preset_name, preset_folder):
    # Проверяем наличие файла с именем preset_name
    files_type = ".txt"
    raw_list = listdir(preset_folder)
    files_names = []
    for file in raw_list:
        if file[-len(files_type):] == files_type:
            files_names.append(file[:-len(files_type)])
    if preset_name not in files_names:
        raise Exception(f"Файл {preset_name}.txt не найден")

    # Читаем файл
    path_to_preset = path.join(preset_folder, preset_name + files_type)
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
