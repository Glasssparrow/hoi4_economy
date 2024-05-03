from constants import (
    FACTORY_COST, MILITARY_FACTORY_COST, INFRASTRUCTURE_COST,
    FACTORY_OUTPUT, MILITARY_FACTORY_OUTPUT, INFRASTRUCTURE_BONUS,
    conscription, economy, trade
)


class Country:

    def __init__(self):
        self.regions = []
        self.constr_bonus = 0
        self.civil_constr_bonus = 0
        self.mil_constr_bonus = 0
        self.mil_output_bonus = 0
        self.factory_limit_bonus = 0

        self.constr_tech = 0
        self.industry_tech = 0
        self.ind_and_constr_tech_limit = 5
        self._distributed_industry = False

        self.factories = 0
        self.mil_factories = 0
        self.factories_available = 0
        self.consumer_goods = 0

    def add_region(self, region):
        self.regions.append(region)

    def add_military_advisor(self):
        self.mil_constr_bonus = 0.1

    def add_civil_advisor(self):
        self.civil_constr_bonus = 0.1

    @property
    def distributed_industry(self):
        return self._distributed_industry

    @distributed_industry.setter
    def distributed_industry(self, boolean):
        if (self.industry_tech != 0
                and self._distributed_industry != boolean):
            raise Exception("Нельзя сменить технологию")
        self._distributed_industry = boolean

    def upgrade_industry_tech(self):
        if self.industry_tech >= 5:
            raise Exception("Лимит технологии 5 уровень")
        elif self._distributed_industry:
            self.mil_output_bonus += 0.1
        else:
            self.mil_output_bonus += 0.15
        self.industry_tech += 1
        self.factory_limit_bonus += 0.2
        for region in self.regions:
            region.recalculate_factories_limit(self.factory_limit_bonus)

    def upgrade_construction_tech(self):
        if self.constr_tech >= 5:
            raise Exception("Лимит технологии 5 уровень")
        else:
            self.constr_tech += 1
            self.constr_bonus += 0.1

    def get_consumer_goods(self):
        return self.consumer_goods

    def add_consumer_goods(self, consumer_goods_modifier):
        self.consumer_goods += consumer_goods_modifier

    def calculate_factories(self):
        civil_fact = 0
        mil_fact = 0
        for region in self.regions:
            civil_fact += region.factories
            mil_fact += region.military_factories
        factories_available = (
            civil_fact - (civil_fact+mil_fact)*self.get_consumer_goods()
        )
        self.factories = civil_fact
        self.mil_factories = mil_fact
        if factories_available > 0:
            self.factories_available = round(factories_available, 0)
        else:
            self.factories_available = 0