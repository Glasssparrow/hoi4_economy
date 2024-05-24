from math import floor as math_floor
from region import Region
from queue import Order
from country import Country
from constants import *


def floor(number):
    cut_fluctuation = round(number, 4)
    return math_floor(cut_fluctuation)


def get_france():
    core = "fra"
    country = Country("France", tag="fra")
    country.add_region(Region(
        "Nord Pas De Calais", [core],
        8,
        4, 3, 0
    ))
    country.add_region(Region(
        "Picardy", [core],
        4,
        4, 1, 0
    ))
    country.add_region(Region(
        "Champagne", [core],
        6,
        4, 1, 0
    ))
    country.add_region(Region(
        "Alsace Lorraine", [core],
        6,
        4, 3, 0
    ))
    country.add_region(Region(
        "Franche Comte", [core],
        6,
        4, 1, 0
    ))
    country.add_region(Region(
        "Bourgogne", [core],
        6,
        4, 2, 0
    ))
    country.add_region(Region(
        "Ile De France", [core],
        10,
        4, 4, 4
    ))
    country.add_region(Region(
        "Normandy", [core],
        6,
        4, 2, 0
    ))
    country.add_region(Region(
        "Loire", [core],
        6,
        4, 1, 0, 1
    ))
    country.add_region(Region(
        "Brittany", [core],
        6,
        3, 0, 0, 5
    ))
    country.add_region(Region(
        "Centre", [core],
        5,
        4, 2, 0
    ))
    country.add_region(Region(
        "Rhone", [core],
        6,
        4, 2, 1
    ))
    country.add_region(Region(
        "Alpes", [core],
        4,
        2, 0, 0
    ))
    country.add_region(Region(
        "Bouches Du Rhone", [core],
        6,
        3, 1, 1, 1, 1
    ))
    country.add_region(Region(
        "Var", [core],
        5,
        3, 0, 0, 3
    ))
    country.add_region(Region(
        "Savoy", [core],
        4,
        2, 0, 0
    ))
    country.add_region(Region(
        "Poitou", [core],
        4,
        3, 1, 0
    ))
    country.add_region(Region(
        "Cetre Sud", [core],
        4,
        3, 0, 0
    ))
    country.add_region(Region(
        "Auvergne", [core],
        4,
        3, 1, 0
    ))
    country.add_region(Region(
        "Limousin", [core],
        5,
        3, 0, 0
    ))
    country.add_region(Region(
        "Languedoc", [core],
        4,
        3, 2, 0
    ))
    country.add_region(Region(
        "Aquitaine", [core],
        6,
        3, 0, 1, 1
    ))

    country.add_region(Region(
        "Pyrenees Atlatiques", [core],
        4,
        3, 0, 0
    ))
    country.add_region(Region(
        "Midi Pyrenees", [core],
        6,
        3, 1, 1
    ))
    country.add_region(Region(
        "Corsica", [core],
        4,
        2, 1, 0
    ))

    country.preparations()
    return country


def get_france_for_tests_2_and_3():
    country = get_france()
    country.add_order(Order(
        region_name="Loire",
        building_type=CIVIL_BUILDING,
        quantity=4,
    ))
    country.add_order(Order(
        region_name="Centre",
        building_type=CIVIL_BUILDING,
        quantity=3,
    ))
    country.add_order(Order(
        region_name="Bourgogne",
        building_type=CIVIL_BUILDING,
        quantity=4,
    ))

    country.preparations()
    return country
