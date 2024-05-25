from json import load
from simulation_code.country import Country
from region import Region


def get_data():
    with open("provinces.txt", "r") as json_file:
        data = load(json_file)
    return data


def get_country(data: dict, name_or_tag: str, by_tag=False):
    name_or_tag = name_or_tag.lower()
    # Ищем название государства. Поднимаем ошибку если не нашли.
    name, tag, not_found = "name_not_found", "tag_not_found", True
    if by_tag:
        tag = name_or_tag
        for number, province_data in data.items():
            if province_data["owner"] == tag:
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
    for number, region_data in data.items():
        if country.tag == region_data["owner"]:
            country.add_region(Region(
                name=region_data["name"],
                global_id=int(number),
                cores=region_data["cores"],
                max_factories=region_data["max_factories"],
                infrastructure=region_data["infrastructure"],
                factories=region_data["factories"],
                military_factories=region_data["military_factories"],
                shipyards=region_data["shipyards"],
                fuel_silo=region_data["fuel_silo"],
                synth_oil=region_data["synth_oil"],
            ))
    country.preparations()
    return country
