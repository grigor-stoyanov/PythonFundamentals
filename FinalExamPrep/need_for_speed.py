n = int(input())
cars = {}
for _ in range(n):
    car, mileage, fuel = input().split('|')
    fuel = int(fuel)
    mileage = int(mileage)
    cars[car] = {'mileage': mileage, 'fuel': fuel}
cmd = input()
while not cmd == 'Stop':
    data = cmd.split(' : ')
    if data[0] == 'Drive':
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if fuel < cars[car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            if cars[car]['mileage'] >= 100000:
                cars.pop(car)
                print('Time to sell the car!')
    elif data[0] == 'Refuel':
        car = data[1]
        fuel = int(data[2])
        cars[car]['fuel'] += fuel
        if cars[car]['fuel'] > 75:
            fuel -= (cars[car['fuel'] - 75])
            cars[car]['fuel'] = 75
        print(f'{car} refueled with {fuel} liters')
    elif data[0] == 'Revert':
        car = data[1]
        mileage = int(data[2])
        cars[car]['mileage'] -= mileage
        if cars[car]['mileage'] < 10000:
            mileage -= (10000 - cars[car]['mileage'])
            cars[car]['mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {mileage} kilometers')
    cmd = input()
cars = dict(sorted(cars.items(), revers=True, key=lambda x: (-x[1]['mileage'], x[0])))
for car, stats in cars.items():
    print(f'{car} -> {stats["mileage"]} kms, Fuel in the tank: {stats["fuel"]} lt.')