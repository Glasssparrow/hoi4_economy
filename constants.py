from laws import Law


FACTORY_COST = 10800
MILITARY_FACTORY_COST = 7200
INFRASTRUCTURE_COST = 6000

FACTORY_OUTPUT = 5
MILITARY_FACTORY_OUTPUT = 10
INFRASTRUCTURE_BONUS = 0.2

# building orders
BUILD_CIVIL_FACTORY = "build_civil_factory"
BUILD_MIL_FACTORY = "build_mil_factory"
BUILD_INFRASTRUCTURE = "build_infrastructure"

# politics orders
ADD_MILITARY_ADVISOR_COMMAND = "military_advisor"
ADD_CIVIL_ADVISOR_COMMAND = "civil_advisor"
CHANGE_INDUSTRY_TYPE_COMMAND = "distributed_industry"
UPGRADE_INDUSTRY_TECH_COMMAND = "industry_tech"
UPGRADE_CONSTRUCTION_TECH_COMMAND = "construction_tech"
PUSH_CONSCRIPTION_COMMAND = "push_conscription"
PUSH_TRADE_COMMAND = "push_trade"
PUSH_ECONOMY_COMMAND = "push_economy"
PULL_CONSCRIPTION_COMMAND = "pull_conscription"
PULL_TRADE_COMMAND = "pull_trade"
PULL_ECONOMY_COMMAND = "pull_economy"
ADD_CONSUMER_GOODS_COMMAND = "add_consumer_goods"
GET_CIVIL_CONSTR_BONUS_COMMAND = "get_civil_constr_bonus"
GET_MIL_CONSTR_BONUS_COMMAND = "get_mil_constr_bonus"
GET_INF_CONSTR_BONUS_COMMAND = "get_inf_constr_bonus"

# Building types
MILITARY_BUILDING = "mil_fact"
CIVIL_BUILDING = "civil_fact"
INF_BUILDING = "infrastructure"


def get_conscription_law():
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
    return conscription


def get_trade_law():
    trade = Law()
    trade.add_law_lvl(name="Free trade", const=0.15, mil_output=0.15)
    trade.add_law_lvl(name="Export focus", const=0.1, mil_output=0.1)
    trade.add_law_lvl(name="Limited exports", const=0.5, mil_output=0.5)
    trade.add_law_lvl(name="Closed economy")
    trade.default_pos = 1
    return trade


def get_economy_law():
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
    return economy
