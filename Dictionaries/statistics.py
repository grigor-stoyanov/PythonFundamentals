cmd = input()
products = {}
while not cmd == 'statistics':
    key, value = cmd.split(': ')
    value = int(value)
    if key in products.keys():
        products[key] += value
    else:
        products[key] = value
    cmd = input()
print('Products in stock:')
for key in products:
    print(f'- {key}: {products[key]}')
print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')