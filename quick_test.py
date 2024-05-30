from read_presets.read_preset import read_preset
from constants_and_settings.constants import (
    PRESETS_PATH, COMMON_TRADE_PATH, COMMON_TECH_PATH
)
from read_presets.preset_into_country import (
    turn_preset_into_country, add_events_to_country
)
from automated_construction.construct_civil_and_mil import (
    auto_construct_without_infrastructure)
from simulation_code.region import Region
from constants_and_settings.constants import CIVIL_BUILDING

# country_preset = read_preset("sov", PRESETS_PATH)
# tech_preset = read_preset("casual", COMMON_TECH_PATH)
# trade_preset = read_preset("sov", COMMON_TRADE_PATH)
# country = turn_preset_into_country(country_preset)
# add_events_to_country(country, trade_preset)
# add_events_to_country(country, tech_preset)

# country_preset = read_preset("sik", PRESETS_PATH)
# country = turn_preset_into_country(country_preset)
#
# auto_construct_without_infrastructure(
#     country, 480, 50, 7,
# )

region = Region(
    "Dzungaria",
    2,
    ["sik"],
    1,
    2,
    0,
    0
)
region.add_queue(2, CIVIL_BUILDING)
