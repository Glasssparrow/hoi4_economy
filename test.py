from tests.test1 import Test1
from tests.test2 import Test2
from tests.test3 import Test3
from tests.test4 import Test4
from tests.test5 import Test5
from tests.test6 import Test6


# Печатать ли результаты
print_text = True

something_wrong = False
for test in [Test1, Test2, Test3, Test4, Test5, Test6]:
    x = test()
    if not x.check(print_text):
        print(f"Тест {x.name} не пройден.")
        something_wrong = True

if not something_wrong:
    print("Все тесты пройдены")
