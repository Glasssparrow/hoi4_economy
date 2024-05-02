from constants import (
    FACTORY_COST, MILITARY_FACTORY_COST, INFRASTRUCTURE_COST,
    FACTORY_OUTPUT, MILITARY_FACTORY_OUTPUT, INFRASTRUCTURE_BONUS,
    conscription, economy, trade
)


class Country:

    def __init__(self):
        self.regions = []
        self.civil_constr_bonus = 0
        self.mil_constr_bonus = 0

    def add_region(self, region):
        self.regions.append(region)

    def add_military_advisor(self):
        self.mil_constr_bonus = 0.1

    def add_civil_advisor(self):
        self.civil_constr_bonus = 0.1
