from read_presets.read_preset import read_preset


result = read_preset("sov")
print(result)
for region in result.regions:
    print(region.name)
