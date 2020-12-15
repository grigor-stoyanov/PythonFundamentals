# класът е инстанция(обект) с определени атрибути и методи
# примвр животно с определен ръст и т.н.
# клас __init__() инициалисира класове/обект който сме съсдали
# dunder методи са методи с double underscore
# special func __init__() наричан още конструктор в който е конвенция да се садават атрибути(добра практика)
# параметър self реферираме към инстанцията(jordan,peter) на конкретния обекта
# имайки 1 клас Person можем да направим n на брой обекти(хора) със атрибути(име,години) и методи
# методите реферират към конкретинте атрибути!
# init атрибутите са прикачени към съответната инстанция
# атрибути прикачени към класа първо се тъси instance атрибут след което class атрибут
# upper cammel case всеки клас
class Person:
    def __init__(self, name):
        self.name = name

        def say_hi(self):
            print(f'hi, my name is {self.name}')
class Animal:
    species = 'Monkeys'

jordan = Person("Jordan Djambasov")
peter = Person("Peter Petrov")
jordan = Animal()
jordan.spiecies
peter.say_hi()
jordan.say_hi()
