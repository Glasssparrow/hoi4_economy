

def _add_queue(country, switch_point, counter=0):
    regions = country.regions
    queue = country.queue
    return counter


def auto_construct_without_infrastructure(
        country, simulation_length, cycle_length, switch_point=0
):
    counter = _add_queue(country, switch_point,)
    for day in simulation_length:
        country.calculate_day(day)
        if day % cycle_length == 0:
            counter = _add_queue(country, switch_point, counter=counter)

