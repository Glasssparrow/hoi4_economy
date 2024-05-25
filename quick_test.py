# comp100 = -0.083
# comp95 = -0.079
# comp70 = -0.058
#
# print(f"{comp70/70}:{comp70}/{-0.00083*70}",
#       f"{comp95/95}:{comp95}/{-0.00083*95}",
#       f"{comp100/100}:{comp100}/{-0.00083*100}")

from tests import *


# Печатать ли результаты
print_text = True

for test in [Core, NonCore]:
    x = test()
    for region in x.country.non_core_regions:
        print(x.country.name, region.name, region.global_id)

