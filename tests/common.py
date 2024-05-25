from math import floor as math_floor
from simulation_code.region import Region
from queue import Order
from simulation_code.country import Country
from constants_and_settings.constants import *


def floor(number):
    cut_fluctuation = round(number, 4)
    return math_floor(cut_fluctuation)


def get_france():
    core = "fra"
    country = Country("France", tag="fra")
    country.add_region(Region(
        "Nord Pas De Calais",
        1,
        [core],
        8,
        4,
        3,
        0
    ))
    country.add_region(Region(
        "Picardy",
        2,
        [core],
        4,
        4,
        1,
        0
    ))
    country.add_region(Region(
        "Champagne",
        3,
        [core],
        6,
        4,
        1,
        0
    ))
    country.add_region(Region(
        "Alsace Lorraine",
        4,
        [core],
        6,
        4,
        3,
        0
    ))
    country.add_region(Region(
        "Franche Comte",
        5,
        [core],
        6,
        4,
        1,
        0
    ))
    country.add_region(Region(
        "Bourgogne",
        6,
        [core],
        6,
        4,
        2,
        0
    ))
    country.add_region(Region(
        "Ile De France",
        7,
        [core],
        10,
        4,
        4,
        4
    ))
    country.add_region(Region(
        "Normandy",
        8,
        [core],
        6,
        4,
        2,
        0
    ))
    country.add_region(Region(
        "Loire",
        9,
        [core],
        6,
        4,
        1,
        0,
        1
    ))
    country.add_region(Region(
        "Brittany",
        10,
        [core],
        6,
        3,
        0,
        0,
        5
    ))
    country.add_region(Region(
        "Centre",
        11,
        [core],
        5,
        4,
        2,
        0
    ))
    country.add_region(Region(
        "Rhone",
        12,
        [core],
        6,
        4,
        2,
        1
    ))
    country.add_region(Region(
        "Alpes",
        13,
        [core],
        4,
        2,
        0,
        0
    ))
    country.add_region(Region(
        "Bouches Du Rhone",
        14,
        [core],
        6,
        3,
        1,
        1,
        1,
        1
    ))
    country.add_region(Region(
        "Var",
        15,
        [core],
        5,
        3,
        0,
        0,
        3
    ))
    country.add_region(Region(
        "Savoy",
        16,
        [core],
        4,
        2,
        0,
        0
    ))
    country.add_region(Region(
        "Poitou",
        17,
        [core],
        4,
        3,
        1,
        0
    ))
    country.add_region(Region(
        "Cetre Sud",
        18,
        [core],
        4,
        3,
        0,
        0
    ))
    country.add_region(Region(
        "Auvergne",
        19,
        [core],
        4,
        3,
        1,
        0
    ))
    country.add_region(Region(
        "Limousin",
        20,
        [core],
        5,
        3,
        0,
        0
    ))
    country.add_region(Region(
        "Languedoc",
        21,
        [core],
        4,
        3,
        2,
        0
    ))
    country.add_region(Region(
        "Aquitaine",
        22,
        [core],
        6,
        3,
        0,
        1,
        1
    ))

    country.add_region(Region(
        "Pyrenees Atlatiques",
        1,
        [core],
        4,
        3,
        0,
        0
    ))
    country.add_region(Region(
        "Midi Pyrenees",
        1,
        [core],
        6,
        3,
        1,
        1
    ))
    country.add_region(Region(
        "Corsica",
        1,
        [core],
        4,
        2,
        1,
        0
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
