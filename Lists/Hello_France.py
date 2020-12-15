items_and_prices = input()
item_list = items_and_prices.split("|")
budget = float(input())
resell_value = []
profit = 0
for each in range(0, len(item_list)):
    items = item_list[each].split("->")
    if items[0] == 'Clothes' and not (float(items[1]) > 50):
        if budget - float(items[1]) >= 0:
            budget -= float(items[1])
            resell_value.append(float(items[1]))
        else:
            continue
    elif items[0] == 'Shoes' and not (float(items[1]) > 35):
        if budget - float(items[1]) >= 0:
            budget -= float(items[1])
            resell_value.append(float(items[1]))
        else:
            continue
    elif items[0] == 'Accessories' and not (float(items[1]) > 20.50):
        if budget - float(items[1]) >= 0:
            budget -= float(items[1])
            resell_value.append(float(items[1]))
        else:
            continue
    else:
        continue
    if budget == 0:
        break
for i in range(0, len(resell_value)):
    print(f'{1.4*resell_value[i]:.2f}', end=" ")
    profit += 1.4*resell_value[i]-resell_value[i]
print(f'\nProfit: {profit:.2f}')
budget += sum([i*1.4 for i in resell_value])
if budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
