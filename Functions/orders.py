def calc_order(product, quantity):
    price = 0
    if product == 'coffee':
        price = 1.5
    elif product == 'water':
        price = 1
    elif product == 'coke':
        price = 1.4
    elif product == 'snacks':
        price = 2
    price = price * quantity
    return price


order = input()
number = int(input())
print(f'{calc_order(order,number):.2f}')