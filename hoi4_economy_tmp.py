from os import path, listdir
from simulation_code.create_a_country import get_data, get_country
from simulation_code.events import Event


def get_instructions_dict():
    # Читаются все файлы формата ".txt".
    # Файл должен содержать название страны или её тэг
    # в первой не закомментированной строке.
    files_type = ".txt"
    raw_list = listdir("simulation_orders")
    files_list = []  # Пути ко всем файлам с инструкциями
    files_names = []
    for file in raw_list:
        if file[-len(files_type):] == files_type:
            files_names.append(file[:-len(files_type)])
            files_list.append(path.join("simulation_orders", file))
    raw_strings = []  # Строки данных из файлов с инструкциями
    for file in files_list:
        with open(file, encoding="utf8") as link_to_the_file:
            raw_strings.append(link_to_the_file.read())
    simulations_instructions = {}  # Список листов с приказами
    for file_number, string in enumerate(raw_strings):
        splitted_string = string.split("\n")
        orders_list = []
        for line in splitted_string:
            edited_line = line.strip()
            if "#" in edited_line:  # Убираем комментарии
                edited_line = edited_line.split("#")[0]
                edited_line = edited_line.strip()
            if edited_line:  # Все не пустые строки в приказы
                orders_list.append(edited_line)
        simulations_instructions[files_names[file_number]] = orders_list
    return simulations_instructions


def simulate(simulations_instructions, length_of_simulation, print_all=False):
    # Необходимые для расчета данные
    with open("tags.txt", "r") as json_file:
        all_tags = json_file.read()
    data = get_data()

    results = {}  # Для итоговых экземпляров стран
    best_result = None
    for file_name, orders in simulations_instructions.items():
        if orders[0].upper() not in all_tags:
            by_tag = False
        else:
            by_tag = True
        # Оставляем только ивенты в списке приказов,
        # а также передаем название/тэг в переменную.
        name_or_tag = orders.pop(0)
        country = get_country(data=data, name_or_tag=name_or_tag, by_tag=by_tag)
        results[file_name] = country
        for order in orders:
            country.add_event(Event(order))
        for x in range(length_of_simulation):
            country.calculate_day(x)
        if print_all:
            print(
                f"Файл {file_name}, страна {country.name} ({country.tag}).\n"
                f"Фабрик - {country.factories}, заводов {country.mil_factories}."
            )
        if best_result:
            if country.mil_factories > results[best_result].mil_factories:
                best_result = file_name
            elif (
                country.mil_factories == results[best_result].mil_factories and
                country.factories > results[best_result].factories
            ):
                best_result = file_name
        else:
            best_result = file_name
    print(f"Лучший результат {best_result}, "
          f"страна {results[best_result].name} "
          f"({results[best_result].tag}). "
          f"Фабрик - {results[best_result].factories}, "
          f"Заводов - {results[best_result].mil_factories}")


def help_get_regions(simulation_instruction, day_x=0):
    with open("tags.txt", "r") as json_file:
        all_tags = json_file.read()
    data = get_data()

    if simulation_instruction[0].upper() not in all_tags:
        by_tag = False
    else:
        by_tag = True
    # Оставляем только ивенты в списке приказов,
    # а также передаем название/тэг в переменную.
    name_or_tag = simulation_instruction.pop(0)
    country = get_country(data=data, name_or_tag=name_or_tag, by_tag=by_tag)
    for order in simulation_instruction:
        country.add_event(Event(order))
    for x in range(day_x):
        country.calculate_day(x)
    for region in country.regions:
        print(
            f"{region.name}, лимит - {region.factories_limit}, "
            f"слотов свободно фабрики/инфраструктура - "
            f"{region.available_for_queue}/{region.available_for_infrastructure}.\n"
            f"Фабрики/заводы - {region.factories}/{region.military_factories}, "
            f"инфраструктура - {region.infrastructure}."
        )


inst = get_instructions_dict()
# help_get_regions(inst["not_paranoic_sov"])
simulate(inst, 730)
