from os import path, listdir
from json import dump

PATH = "provinces"
FORMATS_LIST = ".txt"

comp100 = -0.083
comp95 = -0.079
comp70 = -0.058

print(f"{comp70/70}:{comp70}/{-0.00083*70}",
      f"{comp95/95}:{comp95}/{-0.00083*95}",
      f"{comp100/100}:{comp100}/{-0.00083*100}")
