from read_presets.read_preset import read_preset
from constants_and_settings.constants import (
    PRESETS_PATH, COMMON_TRADE_PATH, COMMON_TECH_PATH
)
from read_presets.preset_into_country import (
    turn_preset_into_country, add_events_to_country
)

country_preset = read_preset("sov", PRESETS_PATH)
tech_preset = read_preset("casual", COMMON_TECH_PATH)
trade_preset = read_preset("sov", COMMON_TRADE_PATH)
country = turn_preset_into_country(country_preset)
add_events_to_country(country, trade_preset)
add_events_to_country(country, tech_preset)
a = 0
for event in country.events:
    a += 1

print(a)
