from create_a_country import get_data, get_country


class NonCore:
    name = "Проверка не национальных территорий (Франция)"

    def __init__(self):
        data = get_data()
        self.country = get_country(data=data, name_or_tag="FRA", by_tag=True)
        self.factories = 33
        self.mil_factories = 8
        self.shipyards = 11

    def check(self, text=False):
        if (
            self.factories == self.country.factories and
            self.mil_factories == self.country.mil_factories and
            self.shipyards == self.country.shipyards
        ):
            return True
        else:
            if text:
                print(
                    f"Целевые показатели:    фабрики/в.заводы/верфи "
                    f"{self.factories}/{self.mil_factories}/{self.shipyards}.\n"
                    f"Полученные результаты: фабрики/в.заводы/верфи "
                    f"{self.country.factories}/"
                    f"{self.country.mil_factories}/"
                    f"{self.country.shipyards}."
                )
                return False
