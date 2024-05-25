from constants_and_settings.constants import *
from simulation_code.queue import Order


class Event:

    def __init__(self, order_text):
        self.order = self._order_from_text(order_text)
        self.date = int(self.order[0])

    def activate(self, owner):
        if self.order[1] in BUILD_CIVIL_FACTORY:
            owner.add_order(Order(
                region_name=self.order[2],
                building_type=CIVIL_BUILDING,
                quantity=int(self.order[3])
            ))
        elif self.order[1] in BUILD_MIL_FACTORY:
            owner.add_order(Order(
                region_name=self.order[2],
                building_type=MILITARY_BUILDING,
                quantity=int(self.order[3])
            ))
        elif self.order[1] in BUILD_INFRASTRUCTURE:
            owner.add_order(Order(
                region_name=self.order[2],
                building_type=INF_BUILDING,
                quantity=int(self.order[3])
            ))
        elif self.order[1] in ADD_MILITARY_ADVISOR_COMMAND:
            owner.add_military_advisor()
        elif self.order[1] in ADD_CIVIL_ADVISOR_COMMAND:
            owner.add_civil_advisor()
        elif self.order[1] in CHANGE_INDUSTRY_TYPE_COMMAND:
            owner.distributed_industry = True
        elif self.order[1] in UPGRADE_INDUSTRY_TECH_COMMAND:
            owner.upgrade_industry_tech()
        elif self.order[1] in UPGRADE_CONSTRUCTION_TECH_COMMAND:
            owner.upgrade_construction_tech()
        elif self.order[1] in PUSH_CONSCRIPTION_COMMAND:
            owner.move_conscription(+1)
        elif self.order[1] in PULL_CONSCRIPTION_COMMAND:
            owner.move_conscription(-1)
        elif self.order[1] in PUSH_TRADE_COMMAND:
            owner.move_trade(+1)
        elif self.order[1] in PULL_TRADE_COMMAND:
            owner.move_trade(-1)
        elif self.order[1] in PUSH_ECONOMY_COMMAND:
            owner.move_economy(+1)
        elif self.order[1] in PULL_ECONOMY_COMMAND:
            owner.move_economy(-1)
        elif self.order[1] in ADD_CONSTR_BONUS_COMMAND:
            owner.add_construction_bonus(
                float(self.order[2]))
        elif self.order[1] in ADD_CIVIL_CONSTR_BONUS_COMMAND:
            owner.add_civil_construction_bonus(
                float(self.order[2]))
        elif self.order[1] in ADD_MIL_CONSTR_BONUS_COMMAND:
            owner.add_mil_construction_bonus(
                float(self.order[2]))
        elif self.order[1] in ADD_INF_CONSTR_BONUS_COMMAND:
            owner.add_inf_construction_bonus(
                float(self.order[2]))
        elif self.order[1] in ADD_CONSUMER_GOODS_COMMAND:
            owner.add_consumer_goods(
                float(self.order[2]))
        elif self.order[1] in SET_NEW_COMPLIANCE_GROW_BONUS:
            owner.compliance_grow = float(self.order[2])
        elif self.order[1] in SET_TRADE_FACTORIES:
            owner.factories_from_trade = int(self.order[2])
        elif self.order[1] in START_WAR:
            owner.peace = False
        else:
            raise Exception(f"{self.order} не корректное событие!")

    @staticmethod
    def _order_from_text(order_text):
        order = order_text.rsplit()
        return order
