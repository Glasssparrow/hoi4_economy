from simulation_code.laws import Law


FACTORY_COST = 10800
MILITARY_FACTORY_COST = 7200
INFRASTRUCTURE_COST = 6000

FACTORY_OUTPUT = 5
MILITARY_FACTORY_OUTPUT = 10
INFRASTRUCTURE_BONUS = 0.2

# building orders
BUILD_CIVIL_FACTORY = [
    "build_civil_factory",
    "построить_гражданскую_фабрику",
]
BUILD_MIL_FACTORY = [
    "build_mil_factory",
    "построить_военный_завод",
]
BUILD_INFRASTRUCTURE = [
    "build_infrastructure",
    "построить_инфраструктуру",
]

# politics orders
ADD_MILITARY_ADVISOR_COMMAND = [
    "military_advisor",
    "добавить_военного_советника",
]
ADD_CIVIL_ADVISOR_COMMAND = [
    "civil_advisor",
    "добавить_гражданского_советника",
]
CHANGE_INDUSTRY_TYPE_COMMAND = [
    "distributed_industry",
    "переключиться_на_распределенную_промышленность"
]
UPGRADE_INDUSTRY_TECH_COMMAND = [
    "industry_tech",
    "изучить_технологию_промышленности"
]
UPGRADE_CONSTRUCTION_TECH_COMMAND = [
    "construction_tech",
    "изучить_технологию_строительства"
]
PUSH_CONSCRIPTION_COMMAND = [
    "push_conscription",
    "продвинуть_призыв",
]
PUSH_TRADE_COMMAND = [
    "push_trade",
    "продвинуть_торговлю",
]
PUSH_ECONOMY_COMMAND = [
    "push_economy",
    "продвинуть_экономику",
]
PULL_CONSCRIPTION_COMMAND = [
    "pull_conscription",
    "отодвинуть_призыв",
]
PULL_TRADE_COMMAND = [
    "pull_trade",
    "отодвинуть_торговлю",
]
PULL_ECONOMY_COMMAND = [
    "pull_economy",
    "отодвинуть_экономику",
]

ADD_CONSTR_BONUS_COMMAND = [
    "add_constr_bonus",
    "добавить_бонус_строительства",
]
ADD_CIVIL_CONSTR_BONUS_COMMAND = [
    "add_civil_constr_bonus",
    "добавить_бонус_гражданского_строительства",
]
ADD_MIL_CONSTR_BONUS_COMMAND = [
    "add_mil_constr_bonus",
    "добавить_бонус_военного_строительства",
]
ADD_INF_CONSTR_BONUS_COMMAND = [
    "add_inf_constr_bonus",
    "добавить_бонус_строительства_инфраструктуры",
]

ADD_CONSUMER_GOODS_COMMAND = [
    "add_consumer_goods",
    "добавить_товары_народного_потребления",
]
ADD_FACTORIES_LIMIT = [
    "add_factories_limit",
    "добавить_лимит_фабрик",
]
ADD_FACTORIES_COMMAND = [
    "add_factories",
    "добавить_фабрики",
]
ADD_MILITARY_FACTORIES_COMMAND = [
    "add_military_factories",
    "добавить_военные_заводы",
]
SET_NEW_COMPLIANCE_GROW_BONUS = [
    "set_new_compliance_grow_bonus",
    "установить_новый_бонус_роста_контроля",
]
SET_TRADE_FACTORIES = [
    "set_trade",
    "установить_торговлю",
]
START_WAR = [
    "start_war",
    "Начать_войну",
]

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


PATH_TO_PROVINCES = "./provinces"
GAME_DATA_FILE_TYPE = ".txt"

PRESETS_FOLDER = "presets"
