from constants import *


class Event:

    def __init__(self, date, order_text):
        self.date = date
        self.order = order_text

    def activate(self, owner):
        order = self._order_from_text()
        if order[0] not in [
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
            raise Exception(f"{order} не корректное событие!")

    def _order_from_text(self):
        return [self.order, self.order]
