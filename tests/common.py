from math import floor as math_floor


def floor(number):
    cut_fluctuation = round(number, 4)
    return math_floor(cut_fluctuation)

