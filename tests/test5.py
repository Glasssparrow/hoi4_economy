from .common import floor
from create_a_country import get_data, get_country
from constants import *
from events import Event


class Test5:
    name = "читаем данные Франция"

    def __init__(self):
        data = get_data()
        self.country = get_country(data=data, name_or_tag="France")

    def check(self, text=False):
        return False
