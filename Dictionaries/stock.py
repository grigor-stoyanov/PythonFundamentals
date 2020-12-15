line = input().split()
stock = {line[i]: line[i + 1] for i in range(0, len(line), 2)}
products = [ele for ele in input().split()]
for product in products:
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')