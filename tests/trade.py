from .common import get_france_for_tests_2_and_3
from constants import *
from events import Event
from region import Region


class TradeFrance:
    name = "Проверка торговли (Франция)"

    def __init__(self):
        self.country1 = get_france_for_tests_2_and_3()
        self.country2 = get_france_for_tests_2_and_3()
        self.country1.move_trade(+1)
        self.country1.move_trade(+1)
        self.country2.move_trade(+1)
        self.country2.move_trade(+1)
        self.country1.factories_from_trade = 10
        self.country2.add_region(Region(
            "unicorn_land",
            999,
            ["fra"],
            10,
            5,
            10,
            0,
            0
        ))
        for country in [self.country1, self.country2]:
            country.add_event(Event(
                f"365 {ADD_CIVIL_ADVISOR_COMMAND[0]}"
            ))
            country.add_event(Event(
                f"365 {PUSH_ECONOMY_COMMAND[0]}"
            ))
            country.add_event(Event(
                f"365 {PUSH_ECONOMY_COMMAND[0]}"
            ))
            country.preparations()
        # Капитан индустрии + частичная мобилизация 1 января 1937

    def check(self, text=False):
        no_problems = True
        incorrect = {}
        for day in range(731):
            self.country1.calculate_day(day)
            self.country2.calculate_day(day)
            if self.country1.factories != (self.country2.factories-10):
                incorrect[day] = [self.country1.factories,
                                  self.country2.factories-10,]
        if incorrect:
            if text:
                print(f"Не совпавшие дни: {incorrect}")
            return False
        return no_problems
