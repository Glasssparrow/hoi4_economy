from read_presets.read_preset import read_preset
from read_presets.preset_into_country import turn_preset_into_country


result = read_preset("sov")
country = turn_preset_into_country(result)
for region in country.regions:
    print(region.name)
