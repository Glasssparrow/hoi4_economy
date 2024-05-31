from constants_and_settings.constants import *
from math import floor


class Region:

    def __init__(self, name, global_id, cores,
                 max_factories, infrastructure,
                 factories, military_factories,
                 shipyards=0, fuel_silo=0, synth_oil=0,):
        self.name = name
        self.global_id = global_id
        self.cores = cores
        self.compliance = None
        # limits
        self.factories_limit = max_factories
        self.init_fact_limit = max_factories
        self.infrastructure_limit = 5
        # factories
        self.infrastructure = infrastructure
        self.factories = factories
        self.military_factories = military_factories
        self.shipyards = shipyards
        self.fuel_silo = fuel_silo
        self.synth_oil = synth_oil
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
        # slots reserver for queue
        self.slot_for_queue = 0
        self.infrastructure_queue_slots = 0
        # slots available
        self.available_for_construction = 0
        self.available_for_queue = 0
        self.available_for_infrastructure = 0
        self.available_for_infrastructure_queue = 0
        self._recalculate_available_slots()

    def get_compliance_modifier(self):
        # Для национальных пров. self.compliance = None
        if not self.compliance:
            raise Exception(
                "Попытка вычислить контроль национальной территории."
            )
        industry_percent = self.compliance * 0.65 + 25
        if self.compliance > 40:
            industry_percent += 10
        return industry_percent/100

    def calculate_day(self, compliance_modifier):
        if self.compliance:  # Для национальных пров. self.compliance = None
            grow = (1+compliance_modifier) * 0.075
            decay = self.compliance * 0.00083
            self.compliance += grow - decay
        else:
            raise Exception(
                "Попытка рассчитать рост контроля в национальной провинции."
            )

    def _recalculate_available_slots(self):
        self.available_for_construction = (
                self.factories_limit
                - self.factories
                - self.military_factories
                - self.shipyards
                - self.fuel_silo
                - self.synth_oil
        )
        self.available_for_queue = (
                self.available_for_construction
                - self.slot_for_queue
        )
        self.available_for_infrastructure = (
            self.infrastructure
            - self.infrastructure_queue_slots
        )
        self.available_for_infrastructure_queue = (
            self.available_for_infrastructure
            - self.infrastructure_queue_slots
        )

    def add_queue(self, quantity, building_type):
        if quantity <= 0:
            raise Exception(
                f"Добавление приказа на строительство <= 0 зданий "
                f"в регионе {self.name}"
            )
        if building_type in [MILITARY_BUILDING, CIVIL_BUILDING]:
            self.slot_for_queue += quantity
            self.available_for_queue -= quantity
            if self.available_for_queue < 0:
                raise Exception(
                    "Слишком много зданий в очереди для "
                    f"фабрик/военных_заводов региона {self.name}"
                )
        elif building_type == INF_BUILDING:
            self.infrastructure_queue_slots += quantity
            self.available_for_infrastructure_queue -= quantity
            if self.available_for_infrastructure_queue < 0:
                raise Exception(
                    "Слишком много инфраструктуры в очереди для "
                    f"региона {self.name}."
                )

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
            floor((1+science_bonus)*self.init_fact_limit)
        )
        self._recalculate_available_slots()

    def is_on_construction_limit(self, type_of_building):
        if (
                type_of_building == MILITARY_BUILDING or
                type_of_building == CIVIL_BUILDING
        ):
            if (
                    (self.factories + self.military_factories +
                     self.shipyards + self.fuel_silo + self.synth_oil
                     ) >= self.factories_limit
            ):
                return True
            else:
                return False
        elif type_of_building == INF_BUILDING:
            if self.infrastructure >= self.infrastructure_limit:
                return True
            else:
                return False
        else:
            raise Exception(
                f"Не найден лимит для здания "
                f"{type_of_building} в регионе "
                f"{self.name}")

    def construct(self, factories, type_of_building,
                  civil_constr_bonus=0,
                  mil_constr_bonus=0,
                  inf_constr_bonus=0):
        construction_complete = False
        if self.is_on_construction_limit(type_of_building):
            raise Exception(
                f"Нельзя построить больше {type_of_building} "
                f"в регионе "
                f"{self.name}."
            )
        if type_of_building == MILITARY_BUILDING:
            self.mil_constr_progress += (
                factories * FACTORY_OUTPUT *
                (INFRASTRUCTURE_BONUS * self.infrastructure + 1) *
                (mil_constr_bonus + 1)
            )
            if self.mil_constr_progress > MILITARY_FACTORY_COST:
                self.military_factories += 1
                self.mil_constr_progress -= MILITARY_FACTORY_COST
                construction_complete = True
        elif type_of_building == CIVIL_BUILDING:
            self.civil_constr_progress += (
                    factories * FACTORY_OUTPUT *
                    (INFRASTRUCTURE_BONUS * self.infrastructure + 1) *
                    (civil_constr_bonus + 1)
            )
            if self.civil_constr_progress > FACTORY_COST:
                self.factories += 1
                self.civil_constr_progress -= FACTORY_COST
                construction_complete = True
        elif type_of_building == INF_BUILDING:
            self.inf_constr_progress += (
                    factories * FACTORY_OUTPUT *
                    (INFRASTRUCTURE_BONUS * self.infrastructure + 1) *
                    (inf_constr_bonus + 1)
            )
            if self.inf_constr_progress > INFRASTRUCTURE_COST:
                self.infrastructure += 1
                self.inf_constr_progress -= INFRASTRUCTURE_COST
                construction_complete = True
        else:
            raise Exception("Некорректный тип здания для постройки")
        return construction_complete
