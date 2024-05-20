from constants import *
from queue import Order


class Event:

    def __init__(self, order_text):
        self.order = self._order_from_text(order_text)
        self.date = int(self.order[0])

    def activate(self, owner):
        if self.order[1] == BUILD_CIVIL_FACTORY:
            owner.add_order(Order(
                region_name=self.order[2],
                building_type=CIVIL_BUILDING,
                quantity=int(self.order[3])
            ))
        elif self.order[1] == BUILD_MIL_FACTORY:
            owner.add_order(Order(
                region_name=self.order[2],
                building_type=MILITARY_BUILDING,
                quantity=int(self.order[3])
            ))
        elif self.order[1] == BUILD_INFRASTRUCTURE:
            owner.add_order(Order(
                region_name=self.order[2],
                building_type=INF_BUILDING,
                quantity=int(self.order[3])
            ))
        elif self.order[1] == ADD_MILITARY_ADVISOR_COMMAND:
            owner.add_military_advisor()
        elif self.order[1] == ADD_CIVIL_ADVISOR_COMMAND:
            owner.add_civil_advisor()
        elif self.order[1] == CHANGE_INDUSTRY_TYPE_COMMAND:
            owner.distributed_industry = True
        elif self.order[1] == UPGRADE_INDUSTRY_TECH_COMMAND:
            owner.upgrade_industry_tech()
        elif self.order[1] == UPGRADE_CONSTRUCTION_TECH_COMMAND:
            owner.upgrade_construction_tech()
        elif self.order[1] == PUSH_CONSCRIPTION_COMMAND:
            owner.move_conscription(+1)
        elif self.order[1] == PULL_CONSCRIPTION_COMMAND:
            owner.move_conscription(-1)
        elif self.order[1] == PUSH_TRADE_COMMAND:
            owner.move_trade(+1)
        elif self.order[1] == PULL_TRADE_COMMAND:
            owner.move_trade(-1)
        elif self.order[1] == PUSH_ECONOMY_COMMAND:
            owner.move_economy(+1)
        elif self.order[1] == PULL_ECONOMY_COMMAND:
            owner.move_economy(-1)
        elif self.order[1] == GET_CIVIL_CONSTR_BONUS_COMMAND:
            pass
        elif self.order[1] == GET_MIL_CONSTR_BONUS_COMMAND:
            pass
        elif self.order[1] == GET_INF_CONSTR_BONUS_COMMAND:
            pass
        elif self.order[1] == ADD_CONSUMER_GOODS_COMMAND:
            pass
        else:
            raise Exception(f"{self.order} не корректное событие!")

    @staticmethod
    def _order_from_text(order_text):
        order = order_text.rsplit()
        return order
