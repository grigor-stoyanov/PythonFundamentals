# list comprehention [x for x in y]
data = [int(i) for i in input().split]
# зaмества copy всякакви операции филтрация на листове ect.
# могат да се сложат и условия вътре
result = [num**2 for num in data if num > 0]
result2 = ['even' if num % 2 == 0 else 'odd' for num in data]
data.insert(0,'obj')
data.extend([100,200])
data.pop(0)
data.remove(77)
data.clear()
# lambda е анонимна функция за запазване на повтарящи се действия като в променлива
# винаги връща и няма име
lambda x: int(x)
nums_as_string = [1,2,3]
num = list(map(int,nums_as_string))
num = list(map(lambda x:int(x), nums_as_string))
even = list(filter(lambda x:x % 2 == 0, num))
# list swapping first index then swap value for each
num[0],num[1],num[3] = num[2],num[0],num[1]
# set func extract unique elements from  a list
list(set(num))
# sorted връща сортиран от най-ниския към най-големия
# sorted(x,key=x.index) връща елементите в същия ред