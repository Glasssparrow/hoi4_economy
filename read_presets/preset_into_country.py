from simulation_code.create_a_country import get_data, get_country
from simulation_code.events import Event


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