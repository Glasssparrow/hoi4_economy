from tests.test1 import Test1
from tests.test3 import Test3


# Печатать ли результаты
print_text = True

something_wrong = False
for test in [Test1, Test3]:
    x = test()
    if not x.check(print_text):
        print(f"Тест {x.name} не пройден.")
        something_wrong = True

if not something_wrong:
    print("Все тесты пройдены")
