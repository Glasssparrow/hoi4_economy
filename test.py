from tests.test1 import Test1
from tests.test2 import Test2
from tests.test3 import Test3
from tests.test4 import Test4
from tests.test5 import Test5
from tests.test6 import Test6
from tests.test7 import Test7


# Печатать ли результаты
print_text = True

# Данные по Франции не верны.
# Не знаю что с этим делать, думаю пока оставлю.
# Странно что описание из файлов игры не совпадает с тем что я вижу в игре.
something_wrong = False
for test in [Test1, Test2, Test3, Test4, Test5, Test6, Test7]:
    x = test()
    if not x.check(print_text):
        print(f"Тест {x.name} не пройден.")
        something_wrong = True

if not something_wrong:
    print("Все тесты пройдены")
