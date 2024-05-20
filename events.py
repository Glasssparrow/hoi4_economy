from constants import *


class Event:

    def __init__(self, order_text):
        self.order = self._order_from_text(order_text)

    def activate(self, owner):
        if self.order[0] not in [
            BUILD_CIVIL_FACTORY,
            BUILD_MIL_FACTORY,
            BUILD_INFRASTRUCTURE,

            ADD_MILITARY_ADVISOR_COMMAND,
            ADD_CIVIL_ADVISOR_COMMAND,
            CHANGE_INDUSTRY_TYPE_COMMAND,
            UPGRADE_INDUSTRY_TECH_COMMAND,
            UPGRADE_CONSTRUCTION_TECH_COMMAND,
            CHANGE_CONSCRIPTION_COMMAND,
            CHANGE_TRADE_COMMAND,
            CHANGE_ECONOMY_COMMAND,
            GET_CIVIL_CONSTR_BONUS_COMMAND,
            GET_MIL_CONSTR_BONUS_COMMAND,
            GET_INF_CONSTR_BONUS_COMMAND,
            ADD_CONSUMER_GOODS_COMMAND,
        ]:
            raise Exception(f"{self.order} не корректное событие!")
        return self.order

    @staticmethod
    def _order_from_text(order_text):
        order = order_text.rsplit()
        return order
