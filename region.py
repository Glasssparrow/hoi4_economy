from constants import *


class Region:

    def __init__(self, name,
                 max_factories, infrastructure,
                 factories, military_factories):
        self.name = name
        # limits
        self.factories_limit = max_factories
        self.init_fact_limit = max_factories
        self.infrastructure_limit = 5
        # factories
        self.infrastructure = infrastructure
        self.factories = factories
        self.military_factories = military_factories
        # resources
        self.oil = 0
        self.aluminum = 0
        self.rubber = 0
        self.tungsten = 0
        self.steel = 0
        self.chromium = 0
        # construction progress
        self.civil_constr_progress = 0
        self.mil_constr_progress = 0
        self.inf_constr_progress = 0

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
                  civil_constr_bonus=0,
                  mil_constr_bonus=0,
                  inf_constr_bonus=0):
        if type_of_building == MILITARY_BUILDING:
            self.mil_constr_progress += (
                factories * FACTORY_OUTPUT *
                (mil_constr_bonus + 1)
            )
            if self.mil_constr_progress > MILITARY_FACTORY_COST:
                self.military_factories += 1
                self.mil_constr_progress -= MILITARY_FACTORY_COST
        elif type_of_building == CIVIL_BUILDING:
            self.civil_constr_progress += (
                    factories * FACTORY_OUTPUT *
                    (civil_constr_bonus + 1)
            )
            if self.civil_constr_progress > FACTORY_COST:
                self.factories += 1
                self.civil_constr_progress -= FACTORY_COST
        elif type_of_building == INF_BUILDING:
            self.inf_constr_progress += (
                    factories * FACTORY_OUTPUT *
                    (inf_constr_bonus + 1)
            )
            if self.inf_constr_progress > INFRASTRUCTURE_COST:
                self.infrastructure += 1
                self.inf_constr_progress -= INFRASTRUCTURE_COST
        else:
            raise Exception("Некорректный тип здания для постройки")
