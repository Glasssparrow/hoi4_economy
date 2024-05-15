from constants import conscription, economy, trade


class Country:

    def __init__(self, name):
        self.name = name
        self.regions = []
        self.queue = []
        self.events = []

        self.constr_bonus = 0
        self.civil_constr_bonus = 0
        self.mil_constr_bonus = 0
        self.inf_constr_bonus = 0
        self.mil_output_bonus = 0
        self.factory_limit_bonus = 0

        self.conscription_law = conscription
        self.economy_law = economy
        self.trade_law = trade
        self.list_of_laws = [conscription, economy, trade]

        self.constr_tech = 0
        self.industry_tech = 0
        self.ind_and_constr_tech_limit = 5
        self._distributed_industry = False

        self.factories = 0
        self.mil_factories = 0
        self.factories_available = 0
        self.consumer_goods = 0

    def calculate_day(self):
        self.calculate_factories()
        free_factories = self.factories_available
        queue_position = 0
        factories_for_region = 0
        while free_factories > 0:
            if free_factories > 15:
                factories_for_region = 15
                free_factories += -15
            else:
                factories_for_region = free_factories
                free_factories = 0
            self.regions[self.queue[queue_position]].construct(
                factories_for_region,
                self.queue[queue_position].building_type,
            )

    def add_event(self, event):
        self.events.append(event)

    def preparations(self):
        for cycle in range(len(self.events)-1):
            for i in range(len(self.events)-1):
                if self.events[i].date > self.events[i+1].date:
                    self.events[i], self.events[i+1] = (
                        self.events[i+1], self.events[i])
        # Активируем все ивенты нулевого дня
        while len(self.events) > 0 and self.events[0].date == 0:
            self.events[0].activate(self)
            self.events.pop(0)

    def add_order(self, order):
        for i, region in enumerate(self.regions):
            if order.target_region == region.name:
                order.target_region_id = i
                break
        self.queue.append(order)
        if order.target_region_id is None:
            raise Exception("Регион не найден")

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

    @staticmethod
    def _move_law(number, law):
        if not isinstance(number, (float, int)):
            raise Exception("Wrong type, should be int or float")
        if number > 0:
            law.law_up()
        elif number < 0:
            law.law_down()
        else:
            pass

    def move_conscription(self, number):
        self._move_law(number, self.conscription_law)

    def move_economy(self, number):
        self._move_law(number, self.economy_law)

    def move_trade(self, number):
        self._move_law(number, self.trade_law)

    def get_civ_constr_bonus(self):
        constr_modifier = 1
        for law in self.list_of_laws:
            constr_modifier += law.constr[law.pos]
            constr_modifier += law.civil_constr[law.pos]
        constr_modifier += self.constr_bonus + self.civil_constr_bonus
        return constr_modifier

    def get_mil_constr_bonus(self):
        constr_modifier = 1
        for law in self.list_of_laws:
            constr_modifier += law.constr[law.pos]
            constr_modifier += law.mil_constr[law.pos]
        constr_modifier += self.constr_bonus + self.mil_constr_bonus
        return constr_modifier

    def get_inf_constr_bonus(self):
        constr_modifier = 1
        constr_modifier += self.constr_bonus + self.inf_constr_bonus
        return constr_modifier
