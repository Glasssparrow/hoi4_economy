from queue import Order


class Event:

    def __init__(self, date,
                 order: Order = None,
                 policies: dict = None):
        self.date = date
        self.order = order
        self.policies = policies

    def activate(self, owner):
        pass

    def _activate_policies(self, owner):
        for k, v in self.policies.values():
            if k not in [
                "military_advisor",
                "civil_advisor",
                "distributed_industry",
                "industry_tech",
                "construction_tech",
                "move_conscription",
                "move_trade",
                "move_economy",
                "add_consumer_goods",
                "get_civil_constr_bonus",
                "get_mil_constr_bonus",
                "get_inf_constr_bonus",
            ]:
                raise Exception(f"{k} не корректное событие!")
