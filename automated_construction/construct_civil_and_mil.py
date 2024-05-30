from constants_and_settings.constants import (
    CIVIL_BUILDING, MILITARY_BUILDING
)
from simulation_code.queue import Order


class Counter:

    def __init__(self):
        self.factories = 0
        self.mil_factories = 0


def _get_regions_with_good_infrastructure(regions):
    good_inf_regions = []
    for region in regions:
        if (
            not good_inf_regions or
            (region.available_for_queue > 0 and
             region.infrastructure > good_inf_regions[0].infrastructure)
        ):
            good_inf_regions = [region]
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
        if len(queue) < (country.factories / 15 + queue_length):
            if (
                    counter.factories > switch_point
            ):
                counter.mil_factories += region.available_for_queue
                country.add_order(Order(
                    region_name=region.name,
                    building_type=CIVIL_BUILDING,
                    quantity=region.available_for_queue,
                ))
            elif (
                    counter.factories + region.available_for_queue >
                    switch_point
            ):
                mil_build = (
                        counter.factories + region.available_for_queue -
                        switch_point
                )
                civil_build = region.available_for_queue - mil_build
                counter.factories += civil_build
                counter.mil_factories += mil_build
                country.add_order(Order(
                    region_name=region.name,
                    building_type=CIVIL_BUILDING,
                    quantity=civil_build,
                ))
                country.add_order(Order(
                    region_name=region.name,
                    building_type=MILITARY_BUILDING,
                    quantity=mil_build,
                ))
            elif (
                    counter.factories + region.available_for_queue < switch_point
            ):
                counter.factories += region.available_for_queue
                country.add_order(Order(
                    region_name=region.name,
                    building_type=MILITARY_BUILDING,
                    quantity=region.available_for_queue,
                ))
        else:
            break


def _add_queue(country, switch_point, counter=None,
               queue_length=2, start_point=False,):
    if not counter:
        counter = Counter()
    regions = country.regions
    queue = country.queue
    if not start_point:
        if len(queue) < country.factories/15:
            raise Exception("Строительство простаивает!")
    good_inf_regions = _get_regions_with_good_infrastructure(regions)
    _add_queue_for_regions(good_inf_regions, country, switch_point,
                           counter, queue_length)
    return counter


def auto_construct_without_infrastructure(
        country, simulation_length, cycle_length, switch_point=999
):
    counter = _add_queue(country, switch_point, start_point=True)
    for day in range(simulation_length):
        country.calculate_day(day)
        if day % cycle_length == 0:
            counter = _add_queue(country, switch_point, counter=counter)
