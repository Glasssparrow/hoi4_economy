from .common import floor, get_france_for_tests_2_and_3


class Test2:
    name = "День за днем Французский"

    def __init__(self):
        self.country = get_france_for_tests_2_and_3()
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
            self.country.calculate_day(day)
        return no_problems
