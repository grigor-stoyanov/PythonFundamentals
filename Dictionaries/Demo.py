# речника е структура от данни с ключ и стойност
fruit = {'orange': 'portokal', 'apple': 'qbylka'}
# те са unordered и mutable като ключовете трябва да са уникални
print(fruit['orange'])
# викаме по ключове, не по индекси
# метод get() По добрия вариант връща none когато не намери нищо и може да се пренаписва
print(fruit.get('orange'))
print(fruit.get('pear', 'not a word in this dict'))
# ключовете са case sensitive!
my_list = [1, 2, 3]
my_list[1] = 100
fruit['orange'] = 'mandarina'
print(fruit.get('orange'))
fruit['orange'] += 'mandarina'
# когато събираш трябва ключа да съществува
print(fruit.get('orange'))
fruit['cat'] = 'kotka'
print(fruit)
# update добавя стойности от друг речник
fruit.update({'dog': ['kuche', 'jivotno']})
print(fruit)
# ako ъпдейтнем по съществуващ ключ променя value на ключа
# викането на 2 ключа става с цикъл или минаване прес dict-a
# можем да имаме dict v dict ili list v dict pri poveche stoinosti
# итериране прес речник става с цикъл като директно се минава прес ключовете
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
for key in numbers:
    print(key, numbers[key])
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# numbers.items() връща тюпъл който може да се расопакова
for key, value in numbers.items():
    print(key, value)
# така се вадят само ключове или стойности но не е точно лист
print(numbers.keys())
print(numbers.values())
# dict comprehension
nums = [1, 2, 3, 4]
result = {num: num ** 2 for num in nums}
print(result)
# existence
print(2 in nums)
if 'orange' in fruit:
    print(fruit['orange'])
if 'kotka' in fruit.values():
    print('kotka is in dict')
# методи
numbers.clear()
# copy при искане на друго мясо в паметта при един и същ dict
fruit.copy()
from copy import deepcopy

# deepcopy копира nested структури
fruit.pop('orange')
# маха се по ключ като връща и itema key,value = mydict.popitem()
del fruit['apple']
# сортирането
numss = [5, -1, 2, 3, 1]
print(sorted(numss, reverse=True))
# при dict 1vo iterable kolekcia 2ro reverse true/false 3to key lambda func po kakvo da sortira
my_dict = {'Peter': 21, 'George': 19, 'John': 45}
# това което правиш е сортираш елементите от дикта в list от тюпъли по втория елемент(age)
print(dict(sorted(my_dict.items(),key=lambda x: x[0])))
sorted(my_dict)
# ще сортира само по ключове

