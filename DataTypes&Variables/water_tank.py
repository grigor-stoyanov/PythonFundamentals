n = int(input())
capacity = 255
total_liters = 0
for i in range(0, n):
    liters = int(input())
    capacity -= liters
    total_liters += liters
    if capacity < 0:
        print("Insufficient capacity!")
        capacity += liters
        total_liters -= liters
print(total_liters)