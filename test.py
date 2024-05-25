from tests import *


# Печатать ли результаты
print_text = True

# Данные по Франции не верны.
# Не знаю что с этим делать, думаю пока оставлю.
# Странно что описание из файлов игры не совпадает с тем что я вижу в игре.
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
