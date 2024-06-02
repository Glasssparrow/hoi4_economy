from read_presets.read_preset import read_preset
from constants_and_settings.constants import (
    PRESETS_PATH, COMMON_TRADE_PATH, COMMON_TECH_PATH
)
from read_presets.preset_into_country import (
    turn_preset_into_country, add_events_to_country
)
from automated_construction.construct_civil_and_mil import (
    auto_construct_without_infrastructure)
import plotly.graph_objs as go


def run_and_get_country(main_preset, tech, trade, length, cycle, switch_point,
                        queue_length, queue_grow, ):
    country = turn_preset_into_country(main_preset.copy())
    add_events_to_country(country, trade.copy())
    add_events_to_country(country, tech.copy())

    auto_construct_without_infrastructure(
        country=country, simulation_length=length,
        cycle_length=cycle, switch_point=switch_point,
        queue_length=queue_length, queue_grow=queue_grow,
    )
    return country


def run_and_get_points(main_preset, tech, trade, length, cycle, switch_point,
                       queue_length, queue_grow, ):
    country = turn_preset_into_country(main_preset.copy())
    add_events_to_country(country, trade.copy())
    add_events_to_country(country, tech.copy())

    f, m, d = auto_construct_without_infrastructure(
        country=country, simulation_length=length,
        cycle_length=cycle, switch_point=switch_point,
        queue_length=queue_length, queue_grow=queue_grow,
    )
    return f, m, d


def get_points(main_preset_name):
    country_preset = read_preset(main_preset_name, PRESETS_PATH)
    tech_preset = read_preset("casual", COMMON_TECH_PATH)
    trade_preset = read_preset("sov", COMMON_TRADE_PATH)

    mil, switch = [], []
    best_mil = 0
    for switch_point in range(100):
        print(main_preset_name, switch_point)
        current_country = run_and_get_country(
            main_preset=country_preset,
            tech=tech_preset,
            trade=trade_preset,
            length=1825, cycle=210,
            switch_point=switch_point,
            queue_length=5, queue_grow=2
        )
        mil.append(current_country.mil_factories)
        switch.append(switch_point)
        if current_country.mil_factories > best_mil:
            best_mil = current_country.mil_factories
    return switch, mil, best_mil


fig = go.Figure()
for preset_name, graph_name in {
    "sov_basic": "Снятие паранойи",
    "sov_mobilize_economy_first": "Снятие паранойи, но мобилизация до советника",
    "sov_basic_free_trade": "Снятие паранойи+свободная торговля",
    "sov_without_focus_tree": "Без бонусов от фокусов на снятие паранойи",
}.items():
    x, y, max_mil = get_points(preset_name)
    fig.add_trace(go.Scatter(x=x, y=y, name=f"{graph_name}({max_mil})"))
fig.show()
