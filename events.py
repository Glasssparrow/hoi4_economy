from queue import Order
from constants import *


class Event:

    def __init__(self, date,
                 order: Order = None,
                 policies: dict = None):
        self.date = date
        self.order = order
        self.policies = policies

    def activate(self, owner):
        if self.order is None:
            return
        else:
            owner.add_order(self.order)
        self._activate_policies(owner)

    def _activate_policies(self, owner):
        if self.policies is None:
            return
        for k, v in self.policies.values():
            if k not in [
                ADD_MILITARY_ADVISOR_COMMAND,
                ADD_CIVIL_ADVISOR_COMMAND,
                CHANGE_INDUSTRY_TYPE_COMMAND,
                UPGRADE_INDUSTRY_TECH_COMMAND,
                UPGRADE_CONSTRUCTION_TECH_COMMAND,
                CHANGE_CONSCRIPTION_COMMAND,
                CHANGE_TRADE_COMMAND,
                CHANGE_ECONOMY_COMMAND,
                ADD_CONSUMER_GOODS_COMMAND,
                GET_CIVIL_CONSTR_BONUS_COMMAND,
                GET_MIL_CONSTR_BONUS_COMMAND,
                GET_INF_CONSTR_BONUS_COMMAND,
            ]:
                raise Exception(f"{k} не корректное событие!")
