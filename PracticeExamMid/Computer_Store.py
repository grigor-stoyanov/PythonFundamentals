cmd = input()
price = 0
while not (cmd == 'special' or cmd == 'regular'):
    cmd = float(cmd)
    if cmd > 0:
        price += cmd
    else:
        print('Invalid price!')
    cmd = input()
if price != 0:
    taxes = price * 0.2
    if cmd == 'regular':
        price += taxes
        discount = price
    elif cmd == 'special':
        price += taxes
        discount = price * 0.90
    print(f"Congratulations you've just bought a new computer!\n\
Price without taxes: {price - taxes:0.2f}$\n\
Taxes: {taxes:0.2f}$\n\
-----------\n\
Total price: {discount:0.2f}$")
else:
    print("Invalid order!")