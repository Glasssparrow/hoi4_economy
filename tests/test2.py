from region import Region
from queue import Order
from country import Country
from constants import *


country = Country("France")
country.add_region(Region(
    "Nord Pas De Calais", 8,
    4, 3, 0
))
country.add_region(Region(
    "Picardy", 4,
    4, 1, 0
))
country.add_region(Region(
    "Champagne", 6,
    4, 1, 0
))
country.add_region(Region(
    "Alsace Lorraine", 6,
    4, 3, 0
))
country.add_region(Region(
    "Franche Comte", 6,
    4, 1, 0
))
country.add_region(Region(
    "Bourgogne", 6,
    4, 2, 0
))
country.add_region(Region(
    "Ile De France", 10,
    4, 4, 4
))
country.add_region(Region(
    "Normandy", 6,
    4, 2, 0
))
country.add_region(Region(
    "Loire", 6,
    4, 1, 0, 1
))
country.add_region(Region(
    "Brittany", 6,
    3, 0, 0, 5
))
country.add_region(Region(
    "Centre", 5,
    4, 2, 0
))
country.add_region(Region(
    "Rhone", 6,
    4, 2, 1
))
country.add_region(Region(
    "Alpes", 4,
    2, 0, 0
))
country.add_region(Region(
    "Bouches Du Rhone", 6,
    3, 1, 1, 1, 1
))
country.add_region(Region(
    "Var", 5,
    3, 0, 0, 3
))
country.add_region(Region(
    "Savoy", 4,
    2, 0, 0
))
country.add_region(Region(
    "Poitou", 4,
    3, 1, 0
))
country.add_region(Region(
    "Cetre Sud", 4,
    3, 0, 0
))
country.add_region(Region(
    "Auvergne", 4,
    3, 1, 0
))
country.add_region(Region(
    "Limousin", 5,
    3, 0, 0
))
country.add_region(Region(
    "Languedoc", 4,
    3, 2, 0
))
country.add_region(Region(
    "Aquitaine", 6,
    3, 0, 1, 1
))
country.add_region(Region(
    "", 0,
    0, 0, 0
))

country.add_region(Region(
    "Pyrenees Atlatiques", 4,
    3, 0, 0
))
country.add_region(Region(
    "Midi Pyrenees", 6,
    3, 1, 1
))
country.add_region(Region(
    "Corsica", 4,
    2, 1, 0
))

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


class Test2:
    name = "Упрощенный Французский"

    def __init__(self):
        self.country = country
        self.factories365 = 32
        self.factories730 = 5555

    def check(self, text=False):
        result1, result2 = 0, 0  # Переменные для записи результата
        for x in range(365):
            self.country.calculate_day()
            result1 = self.country.factories
        for y in range(365):
            self.country.calculate_day()
            result2 = self.country.factories
        if (
                self.factories365 == self.country.factories
        ):
            return True
        else:
            if text:
                print(
                    f"Результаты теста {self.name}\n"
                    f"Целевой результат:"
                    f"1 год - {self.factories365}, "
                    f"2 года - {self.factories730}.\n"
                    f"Полученный результат: "
                    f"1 год - {result1}, "
                    f"2 года - {result2}."
                )
            return False
