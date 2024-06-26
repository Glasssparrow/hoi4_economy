from constants_and_settings.constants import (
    CIVIL_BUILDING, MILITARY_BUILDING
)
from simulation_code.queue import Order


class Counter:

    def __init__(self):
        self.factories = 0
        self.mil_factories = 0
        self.cycles = 0


def _get_regions_with_good_infrastructure(regions):
    there_no_slots_in_core_regions = True
    for region in regions:
        if region.compliance is None and region.available_for_queue > 0:
            there_no_slots_in_core_regions = False
            break
    good_inf_regions = []
    for region in regions:
        # Если нет слотов в нац территориях и территория нац, пропускаем
        if there_no_slots_in_core_regions and region.compliance is None:
            continue
        # Если есть слоты в нац территориях и территория не нац, пропускаем
        elif not there_no_slots_in_core_regions and region.compliance is not None:
            continue
        # Если на территории нет свободных слотов, пропускаем
        if region.available_for_queue == 0:
            continue
        # Если список good_inf_regions пуст или найдена территория
        # с лучшей инфраструктурой и свободными слотами,
        # начинаем список с начала, первый элемент - текущая территория.
        if (
            not good_inf_regions or
            (region.available_for_queue > 0 and
             region.infrastructure > good_inf_regions[0].infrastructure)
        ):
            good_inf_regions = [region]
        # Если территория с такой же инфраструктурой и свободными слотами,
        # добавляем её в лист.
        elif (
                (good_inf_regions[0].infrastructure ==
                 region.infrastructure) and
                region.available_for_queue > 0
        ):
            good_inf_regions.append(region)
    return good_inf_regions


def _add_queue_for_regions(regions, country, switch_point,
                           counter, queue_length):
    queue = country.queue
    for region in regions:
        if region.available_for_queue == 0:
            raise Exception(
                f"{region.name} 0 slots"
            )
        if len(queue) < (country.factories / 15 + queue_length):

            if (
                counter.factories + region.available_for_queue <= switch_point
            ):
                counter.factories += region.available_for_queue
                country.add_order(Order(
                    region_name=region.name,
                    building_type=CIVIL_BUILDING,
                    quantity=region.available_for_queue,
                ))

            elif (
                    counter.factories >= switch_point
            ):
                counter.mil_factories += region.available_for_queue
                country.add_order(Order(
                    region_name=region.name,
                    building_type=MILITARY_BUILDING,
                    quantity=region.available_for_queue,
                ))

            else:
                civil_build = switch_point - counter.factories
                mil_build = (
                        region.available_for_queue - civil_build
                )
                counter.factories += civil_build
                counter.mil_factories += mil_build
                if civil_build > 0:
                    country.add_order(Order(
                        region_name=region.name,
                        building_type=CIVIL_BUILDING,
                        quantity=civil_build,
                    ))
                else:
                    raise Exception(
                        f"Строительство 0 фабрик {region.name}"
                    )
                if mil_build > 0:
                    country.add_order(Order(
                        region_name=region.name,
                        building_type=MILITARY_BUILDING,
                        quantity=mil_build,
                    ))
                else:
                    raise Exception(
                        f"Строительство 0 фабрик {region.name}"
                    )
        else:
            break


def _add_queue(country, switch_point, queue_length,
               counter=None, start_point=False,):
    if not counter:
        counter = Counter()
    regions = country.regions
    queue = country.queue
    if not start_point:
        if (
            country.factories/15 > len(queue) and
            country.get_amount_of_regions_with_free_slots() != 0
        ):
            raise Exception("Строительство простаивает!")
    for x in range(5):
        good_inf_regions = _get_regions_with_good_infrastructure(regions)
        _add_queue_for_regions(good_inf_regions, country, switch_point,
                               counter, queue_length)
        if len(queue) >= (country.factories / 15 + queue_length):
            break
    return counter


def auto_construct_without_infrastructure(
        country, simulation_length, cycle_length, switch_point=999,
        queue_length=3, queue_grow=1
):
    counter = _add_queue(country=country, switch_point=switch_point,
                         start_point=True, queue_length=queue_length)
    factories, mil_factories, days = [], [], []
    for day in range(simulation_length):
        country.calculate_day(day)

        # Заполняем листы для графиков
        factories.append(country.factories)
        mil_factories.append(country.mil_factories)
        days.append(day)

        # Заполняем очередь.
        if day % cycle_length == 0:
            counter.cycles += 1
            counter = _add_queue(
                country=country, switch_point=switch_point,
                counter=counter,
                queue_length=queue_length+queue_grow*counter.cycles,
            )
    return factories, mil_factories, days
