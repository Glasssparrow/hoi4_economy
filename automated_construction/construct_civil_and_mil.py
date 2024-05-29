

class Counter:

    def __init__(self):
        self.number = 0


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


def _add_queue(country, switch_point, counter=None):
    if not counter:
        counter = Counter()
    regions = country.regions
    queue = country.queue
    good_inf_regions = _get_regions_with_good_infrastructure(regions)
    return counter


def auto_construct_without_infrastructure(
        country, simulation_length, cycle_length, switch_point=5000
):
    counter = _add_queue(country, switch_point,)
    for day in range(simulation_length):
        country.calculate_day(day)
        if day % cycle_length == 0:
            counter = _add_queue(country, switch_point, counter=counter)
