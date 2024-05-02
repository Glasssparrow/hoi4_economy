from .laws import Law


FACTORY_COST = 10000
MILITARY_FACTORY_COST = 8000
INFRASTRUCTURE_COST = 6000

FACTORY_OUTPUT = 10
MILITARY_FACTORY_OUTPUT = 10
INFRASTRUCTURE_BONUS = 0.2


conscription = Law()
conscription.add_law_lvl(name="Disarmed nation")
conscription.add_law_lvl(name="Volunteer only")
conscription.add_law_lvl(name="Limited conscription")
conscription.add_law_lvl(name="Extensive conscription")
conscription.add_law_lvl(
    name="Service by requirement",
    const=-0.1, mil_output=-0.1
)
conscription.add_law_lvl(
    name="All adults serve",
    const=-0.3, mil_output=-0.3
)
conscription.add_law_lvl(
    name="Scraping the barrel",
    const=-0.4, mil_output=-0.4
)
conscription.default_pos = 1
trade = Law()
trade.add_law_lvl(name="Free trade", const=0.15, mil_output=0.15)
trade.add_law_lvl(name="Export focus", const=0.1, mil_output=0.1)
trade.add_law_lvl(name="Limited exports", const=0.5, mil_output=0.5)
trade.add_law_lvl(name="Closed economy")
trade.default_pos = 1
economy = Law()
economy.add_law_lvl(
    name="Undisturbed Isolation",
    civil_constr=-0.5, mil_constr=-0.5, cons_goods=0.5)
economy.add_law_lvl(
    name="Isolation",
    civil_constr=-0.4, mil_constr=-0.4, cons_goods=0.4)
economy.add_law_lvl(
    name="Civilian economy",
    civil_constr=-0.3, mil_constr=-0.3, cons_goods=0.35)
economy.add_law_lvl(
    name="Early mobilisation",
    civil_constr=-0.1, mil_constr=-0.1, cons_goods=0.3)
economy.add_law_lvl(
    name="Partial mobilisation",
    civil_constr=0, mil_constr=0.1, cons_goods=0.25)
economy.add_law_lvl(
    name="War economy",
    civil_constr=0, mil_constr=0.2, cons_goods=0.20)
economy.add_law_lvl(
    name="Total mobilisation",
    civil_constr=0, mil_constr=0.3, cons_goods=0.10)
economy.default_pos = 2
