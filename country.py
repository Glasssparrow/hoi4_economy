from constants import (
    get_economy_law, get_trade_law, get_conscription_law)
from math import floor


class Country:

    def __init__(self, name, tag="no tag", start_non_core_compliance=70):
        self.name = name
        self.tag = tag
        self.regions = []
        self.non_core_regions = []
        self.queue = []
        self.events = []

        self._constr_bonus = 0
        self._civil_constr_bonus = 0
        self._mil_constr_bonus = 0
        self._inf_constr_bonus = 0
        self.mil_output_bonus = 0
        self.factory_limit_bonus = 0
        self._consumer_goods = 0
        self.non_core_compliance = start_non_core_compliance
        self.peace = True
        self._compliance_grow = 0

        self._have_civil_advisor = False
        self._have_mil_advisor = False

        self.conscription_law = get_conscription_law()
        self.economy_law = get_economy_law()
        self.trade_law = get_trade_law()
        self.list_of_laws = [
            self.conscription_law, self.economy_law, self.trade_law
        ]

        self.constr_tech = 0
        self.industry_tech = 0
        self.ind_and_constr_tech_limit = 5
        self._distributed_industry = False

        self.factories_total = 0
        self.factories_from_trade = 0
        self.factories = 0
        self.mil_factories = 0
        self.shipyards = 0
        self.factories_available = 0
        self.factories_for_consumers = 0
        self.consumer_goods = 0

    def calculate_day(self, day):
        self.activate_events(day)
        self._daily_compliance_grow()
        self._calculate_factories()
        free_factories = self.factories_available
        queue_position = -1
        civil_constr_bonus = self.civil_constr_bonus
        mil_constr_bonus = self.mil_constr_bonus
        inf_constr_bonus = self.inf_constr_bonus
        empty = []  # Список опустевших заданий на строительство
        while (
                free_factories > 0 and
                queue_position < (len(self.queue)-1)
        ):
            queue_position += 1
            if free_factories > 15:
                factories_for_region = 15
                free_factories += -15
            else:
                factories_for_region = free_factories
                free_factories = 0
            target_region_id = self.queue[queue_position].target_region_id
            done = self.regions[target_region_id].construct(
                factories_for_region,
                self.queue[queue_position].building_type,
                civil_constr_bonus=civil_constr_bonus,
                mil_constr_bonus=mil_constr_bonus,
                inf_constr_bonus=inf_constr_bonus,
            )
            # Если строительство завершено, проверяем нет ли в
            # задании еще зданий, если нет, то добавляем в список
            # пустых заданий на строительство.
            if done:
                order_is_empty = self.queue[queue_position].finish_one()
                if order_is_empty:
                    empty.append(queue_position)
        # Удаляем все пустые задания на строительство
        if len(empty) > 0:
            empty.sort()
            for x in reversed(empty):
                self.queue.pop(x)

    def _daily_compliance_grow(self):
        for region in self.non_core_regions:
            region.calculate_day(self.compliance_grow)

    def add_event(self, event):
        self.events.append(event)

    def preparations(self):
        self._calculate_factories()
        for cycle in range(len(self.events)-1):
            for i in range(len(self.events)-1):
                if self.events[i].date > self.events[i+1].date:
                    self.events[i], self.events[i+1] = (
                        self.events[i+1], self.events[i])
        # Активируем все ивенты нулевого дня
        while len(self.events) > 0 and self.events[0].date == 0:
            self.events[0].activate(self)
            self.events.pop(0)

    def activate_events(self, day):
        done_events = []
        for number, event in enumerate(self.events):
            if event.date == day:
                event.activate(self)
                done_events.append(number)
        for number in reversed(done_events):
            self.events.pop(number)

    def add_order(self, order):
        for i, region in enumerate(self.regions):
            if order.target_region == region.name:
                order.target_region_id = i
                break
        self.queue.append(order)
        if order.target_region_id is None:
            raise Exception("Регион не найден")

    def add_region(self, region, compliance=None):
        if self.tag in region.cores:
            self.regions.append(region)
        elif compliance:
            self.regions.append(region)
            self.non_core_regions.append(region)
            region.compliance = compliance
        else:
            self.regions.append(region)
            self.non_core_regions.append(region)
            region.compliance = self.non_core_compliance

    def add_military_advisor(self):
        if self._have_mil_advisor:
            raise Exception(
                "Уже есть советник на заводы"
            )
        self._mil_constr_bonus += 0.1
        self._have_mil_advisor = True

    def add_civil_advisor(self):
        if self._have_civil_advisor:
            raise Exception(
                "Уже есть советник на фабрики."
            )
        self._civil_constr_bonus += 0.1
        self._inf_constr_bonus += 0.1
        self._have_civil_advisor = True

    @property
    def compliance_grow(self):
        compliance_grow = self._compliance_grow
        if self.peace:
            compliance_grow += 0.1
        return compliance_grow

    @compliance_grow.setter
    def compliance_grow(self, new_compliance_grow):
        self._compliance_grow = new_compliance_grow

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
            self._constr_bonus += 0.1

    def _get_consumer_goods(self):
        cons_goods = self._consumer_goods
        for law in self.list_of_laws:
            cons_goods += law.cons_goods[law.pos]
        return cons_goods

    def add_consumer_goods(self, consumer_goods_modifier):
        self._consumer_goods += consumer_goods_modifier

    def add_construction_bonus(self, bonus):
        self._constr_bonus += bonus

    def add_civil_construction_bonus(self, bonus):
        self._civil_constr_bonus += bonus

    def add_mil_construction_bonus(self, bonus):
        self._mil_constr_bonus += bonus

    def add_inf_construction_bonus(self, bonus):
        self._inf_constr_bonus += bonus

    def _calculate_factories(self):
        civil_fact = 0
        mil_fact = 0
        shipyards = 0
        for region in self.regions:
            if self.tag in region.cores:
                civil_fact += region.factories
                mil_fact += region.military_factories
                shipyards += region.shipyards
            else:
                civil_fact += (
                    region.factories * region.get_compliance_modifier()
                )
                mil_fact += (
                    region.military_factories * region.get_compliance_modifier()
                )
                shipyards += (
                    region.shipyards * region.get_compliance_modifier()
                )
        # Округляем вниз
        civil_fact, mil_fact, shipyards = (
            int(civil_fact), int(mil_fact), int(shipyards))
        self.factories = civil_fact  # Все фабрики государства
        civil_fact += self.factories_from_trade  # Добавляем торговлю
        self.consumer_goods = self._get_consumer_goods()
        self.factories_for_consumers = floor(
                (civil_fact + mil_fact) * self._get_consumer_goods()
        )
        factories_available = (
            civil_fact - self.factories_for_consumers
        )
        self.factories_total = civil_fact
        self.factories = civil_fact - self.factories_from_trade
        self.mil_factories = mil_fact
        self.shipyards = shipyards
        if factories_available > 0:
            self.factories_available = round(factories_available, 0)
        else:
            self.factories_available = 0

    @property
    def civil_constr_bonus(self):
        result = self._constr_bonus
        result += self._civil_constr_bonus
        for law in self.list_of_laws:
            result += law.constr[law.pos]
            result += law.civil_constr[law.pos]
        return result

    @property
    def mil_constr_bonus(self):
        result = self._constr_bonus
        result += self._civil_constr_bonus
        for law in self.list_of_laws:
            result += law.constr[law.pos]
            result += law.civil_constr[law.pos]
        return result

    @property
    def inf_constr_bonus(self):
        result = self._constr_bonus
        result += self._inf_constr_bonus
        for law in self.list_of_laws:
            result += law.constr[law.pos]
        return result

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
        constr_modifier += self._constr_bonus + self._civil_constr_bonus
        return constr_modifier

    def get_mil_constr_bonus(self):
        constr_modifier = 1
        for law in self.list_of_laws:
            constr_modifier += law.constr[law.pos]
            constr_modifier += law.mil_constr[law.pos]
        constr_modifier += self._constr_bonus + self._mil_constr_bonus
        return constr_modifier

    def get_inf_constr_bonus(self):
        constr_modifier = 1
        constr_modifier += self._constr_bonus + self._inf_constr_bonus
        return constr_modifier
