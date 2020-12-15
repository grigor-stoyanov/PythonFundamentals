orders = int(input())
total_price = 0
for _ in range(orders):
        price_capsule = float(input())
        days = int(input())
        count_capsule = float(input())
        coffee_price = ((days*count_capsule)*price_capsule)
        print(f"The price for the coffee is: ${coffee_price:.2f}")
        total_price += coffee_price
print(f"Total: ${total_price:.2f}")