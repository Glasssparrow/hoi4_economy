from region import Region
from queue import Order
from country import Country
from constants import *
from .common import floor


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


class Test3:
    name = "День за днем Французский"

    def __init__(self):
        self.country = country
        self.country.move_trade(+1)
        self.country.move_trade(+1)
        self.factories365 = 32
        self.days = {
            0: (0, 0, 0,),  # старт
            1: (94, 12, 0,),
            2: (189, 25, 0,),
            3: (283, 37, 0,),
            4: (378, 50, 0),
            5: (472, 63, 0),
            6: (567, 75, 0),
            7: (661, 88, 0),  # смотрим 1 неделю
            31: (2929, 390, 0),  # 1 февраля
            59: (5575, 743, 0),  # 1 марта
            90: (8505, 1134, 0),  # 1 апреля
            120: (540, 1512, 0),  # 1 мая
            151: (3469, 1902, 0),  # 1 июня
            181: (6304, 2280, 0),  # 1 июля
            212: (9234, 2671, 0),  # 1 августа
            243: (1363, 3150, 0),  # 1 сентября
            273: (4198, 3717, 0),  # 1 октября
            304: (7128, 4302, 0),  # 1 ноября
            334: (9963, 4869, 0),  # 1 декабря
            337: (10246, 4926, 0),  # 4 декабря
            339: (10435, 4964, 0),  # 6 декабря
            341: (10624, 5002, 0),  # 8 декабря
            343: (13, 5040, 0),  # 10 декабря
            353: (958, 5229, 0),  # 20 декабря
            365: (2092, 5455, 0),  # 1 января
            730: (0, 0, 8643)  # 1 января
        }

    def check(self, text=False):
        region_ids = [8, 10, 5]
        regions = self.country.regions
        no_problems = True
        for day in range(731):
            if day in self.days.keys():
                # print("День #", day)
                # print(self.days[day][0],
                #       self.days[day][1],
                #       self.days[day][2],
                #       " : ",
                #       floor(self.country.regions[8].civil_constr_progress),
                #       floor(self.country.regions[10].civil_constr_progress),
                #       floor(self.country.regions[5].civil_constr_progress),
                #       )

                no_problem_in_the_day = True
                for x in range(3):
                    if (
                        floor(regions[region_ids[x]].civil_constr_progress)
                        != self.days[day][x] and
                        self.days[day][x] != 0
                    ):
                        no_problems = False
                        no_problem_in_the_day = False
                if not no_problem_in_the_day:
                    for_print = []
                    for i in region_ids:
                        for_print.append(floor(
                            regions[i].civil_constr_progress)
                        )
                    if text:
                        print(
                            f"День {day} не совпадает. "
                            f"Ожидаем/получили [{self.days[day][0]}, "
                            f"{self.days[day][1]}, "
                            f"{self.days[day][2]}]/"
                            f"{for_print}. "
                        )
            self.country.calculate_day()
        return no_problems
