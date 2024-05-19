from tests.test1 import Test1


something_wrong = False
for test in [Test1]:
    x = Test1()
    if not x.check():
        print(f"Тест {x.name} не пройден.")
        something_wrong = True

if not something_wrong:
    print("Все тесты пройдены")
