from .common import floor, get_france_for_tests_2_and_3


class AdvisorAndLawFrance:
    name = "с капитаном индустрии Французский"

    def __init__(self):
        self.country = get_france_for_tests_2_and_3()
        self.country.move_trade(+1)
        self.country.move_trade(+1)
        # Капитан индустрии + частичная мобилизация 1 января 1937
        self.days = {
            0: (0, 0, 0,),  # старт
            365: (2092, 5455, 0),  # 1 января 1937
            366: (2241, 5525, 0),  # 2 января 1937
            396: (6696, 7604, 0),  # 1 февраля 1937
            730: (0, 0, 4517)  # 1 января 1938
        }
        # день: (фабрики, военные_заводы, верфи)
        self.industry = {
            0: (29, 8, 11),  # старт
            365: (32, 8, 11),  # 1 января 1937
            366: (32, 8, 11),  # 2 января 1937
            396: (32, 8, 11),  # 1 февраля 1937
            730: (39, 8, 11),  # 1 января 1938
        }

    def check(self, text=False):
        region_ids = [8, 10, 5]
        regions = self.country.regions
        no_problems = True
        for day in range(731):
            if day == 365:
                self.country.add_civil_advisor()
                self.country.move_economy(+1)
                self.country.move_economy(+1)
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
                # Проверяем прогресс строительства в 3 выбранных регионах.
                for x in range(3):
                    if (
                        floor(regions[region_ids[x]].civil_constr_progress)
                        != self.days[day][x] and
                        self.days[day][x] != 0
                    ):
                        no_problems = False
                        no_problem_in_the_day = False
                for index, quantity_of_buildings in {
                    0: self.country.factories,
                    1: self.country.mil_factories,
                    2: self.country.shipyards,
                }.items():
                    if quantity_of_buildings != self.industry[day][index]:
                        no_problems = False
                        no_problem_in_the_day = False

                # Выводим на экран если что-то не сходится
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
                            f"Количество зданий ожидали/получили "
                            f"{self.industry[day]}/"
                            f"({self.country.factories}, "
                            f"{self.country.mil_factories}, "
                            f"{self.country.shipyards})."
                        )
            self.country.calculate_day(day)
        return no_problems
