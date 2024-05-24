from region import Region
from queue import Order
from country import Country
from constants import *
from .common import floor


core = "sik"
country = Country("Sinkiang")
country.add_region(Region(
    "Dabancheng", [core],
    2,
    2, 0, 1
))
country.add_region(Region(
    "Dzungaria", [core],
    1,
    2, 1, 0
))
country.add_region(Region(
    "Kunlun Shan", [core],
    0,
    1, 0, 0
))
country.add_region(Region(
    "Urumqi", [core],
    2,
    2, 2, 0
))
country.add_region(Region(
    "Taklamakan", [core],
    0,
    1, 0, 0
))
country.add_region(Region(
    "Yarkand", [core],
    1,
    1, 1, 0
))
country.add_order(Order(
    region_name="Dabancheng",
    building_type=CIVIL_BUILDING,
    quantity=1,
))

country.preparations()


class Sinkiang:
    name = "Упрощенный Синцзянский"

    def __init__(self):
        self.country = country
        self.constr365 = 6132

    def check(self, text=False):
        for x in range(365):
            self.country.calculate_day(x)
        # print(self.country.regions[0].civil_constr_progress)
        # print(f"Доступно фабрик {self.country.factories_available}")
        # print(self.country.consumer_goods)
        # print(self.country.factories_for_consumers)
        if (
                self.constr365 ==
                floor(self.country.regions[0].civil_constr_progress)
        ):
            return True
        else:
            if text:
                print(
                    f"Результаты теста {self.name}\n"
                    f"Целевой результат {self.constr365}.\n"
                    f"Полученный результат "
                    f"{self.country.regions[0].civil_constr_progress}."
                )
            return False
