from json import load
from country import Country


def get_data():
    with open("provinces.txt", "r") as json_file:
        data = load(json_file)
    return data


def get_country(data, name_or_tag, by_tag=False):
    # Ищем название государства. Поднимаем ошибку если не нашли.
    name, tag, not_found = "name_not_found", "tag_not_found", True
    if by_tag:
        tag = name_or_tag
        for number, province_data in data.items():
            if province_data["owner"] == name_or_tag:
                name = province_data["name"]
                not_found = False
                break
    else:
        name = name_or_tag
        for number, province_data in data.items():
            if province_data["name"] == name_or_tag:
                tag = province_data["owner"]
                not_found = False
                break
    if not_found:
        raise Exception("Country name/tag not found!")

    country = Country(name=name, tag=tag)
