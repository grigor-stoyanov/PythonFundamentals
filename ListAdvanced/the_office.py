happiness = [int(el) for el in input().split()]
factor = int(input())
happiness = list(map(lambda x: x*factor, happiness))
avg = sum(happiness)/len(happiness)
unhappy = [each for each in happiness if each < avg]
print(f'Score:{len(happiness)-len(unhappy)}/{len(happiness)}.',end=" ")
if len(unhappy) <= len(happiness)//2:
    print('Employees are happy!')
else:
    print('Employees are not happy!')
