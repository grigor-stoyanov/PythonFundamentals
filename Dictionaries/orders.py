# cmd = input()
# receipt = {}
# while not cmd == 'buy':
#     name, price, quantity = cmd.split()
#     price = float(price)
#     quantity = int(quantity)
#     if name not in receipt:
#         receipt[name] = [price, quantity]
#     else:
#         receipt[name][1] += quantity
#         receipt[name][0] = price
#     cmd = input()
# for key, value in receipt.items():
#     print(f'{key} -> {value[0]*value[1]:0.2f}')
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.name} -> {self.price*self.quantity:0.2f}'


cmd = input()
products = []

while not cmd == 'buy':
    name, price, quantity = cmd.split()
    price = float(price)
    quantity = int(quantity)
    if name in map(lambda x: x.name, products):
        product = list(filter(lambda x: x.name == name, products))[0]
        product.price = price
        product.quantity += quantity
    else:
        product = Product(name, price, quantity)
        products.append(product)
        cmd = input()
for ele in products:
    print(ele)