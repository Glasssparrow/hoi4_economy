from tests import *


# Печатать ли результаты
print_text = True

# Не национальные территории дают меньше фабрик
something_wrong = False
for test in [Sinkiang, DayAfterDayFrance,
             AdvisorAndLaw, EventsFrance,
             ReadGermany, ReadSoviets,
             Core, NonCore]:
    x = test()
    if not x.check(print_text):
        print(f"Тест {x.name} не пройден.")
        something_wrong = True

if not something_wrong:
    print("Все тесты пройдены")
