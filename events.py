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
