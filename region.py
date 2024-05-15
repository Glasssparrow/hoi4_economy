

class Region:

    def __init__(self, name,
                 max_factories, infrastructure,
                 factories, military_factories):
        self.name = name
        self.factories_limit = max_factories
        self.init_fact_limit = max_factories
        self.infrastructure_limit = 5
        self.infrastructure = infrastructure
        self.factories = factories
        self.military_factories = military_factories
        self.oil = 0
        self.aluminum = 0
        self.rubber = 0
        self.tungsten = 0
        self.steel = 0
        self.chromium = 0

    def add_resources(self, oil, aluminum, rubber,
                      tungsten, steel, chromium):
        self.oil = oil
        self.aluminum = aluminum
        self.rubber = rubber
        self.tungsten = tungsten
        self.steel = steel
        self.chromium = chromium

    def recalculate_factories_limit(self, science_bonus):
        self.factories_limit = (
            round((1+science_bonus)*self.init_fact_limit, 0)
        )

    def construct(self, factories, type_of_building,
                  civil_constr_bonus=0, mil_constr_bonus=0,
                  inf_constr_bonus=0):
        pass

