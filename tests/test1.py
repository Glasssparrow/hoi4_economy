from region import Region
from country import Country


class Test1:
    name = "Name"

    def __init__(self):
        self.country = Country("Sinkiang")
        self.country.add_region(Region(
            "Dabancheng", 2,
            2, 0, 1
        ))
        self.country.add_region(Region(
            "Dzungaria", 1,
            2, 1, 0
        ))
        self.country.add_region(Region(
            "Kunlun Shan", 0,
            1, 0, 0
        ))
        self.country.add_region(Region(
            "Urumqi", 2,
            2, 2, 0
        ))
        self.country.add_region(Region(
            "Taklamakan", 0,
            1, 0, 0
        ))
        self.country.add_region(Region(
            "Yarkand", 1,
            1, 1, 0
        ))
        self.constr365 = 6132

    def check(self):
        for x in range(365):
            self.country.calculate_day()
        return True
