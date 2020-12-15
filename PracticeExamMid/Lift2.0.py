people_waiting = int(input())
lift_state = list(map(int, input().split()))
wagons = []

for lift in lift_state:
    while lift < 4 and people_waiting != 0:
        lift += 1
        people_waiting -= 1
    wagons.append(lift)
wagons_to_str = [str(wagon) for wagon in wagons]

if len(wagons) * 4 == sum(wagons) and people_waiting == 0:
    print(f"{' '.join(wagons_to_str)}")
elif len(wagons) * 4 > sum(wagons) and people_waiting == 0:
    print("The lift has empty spots!\n"
          f"{' '.join(wagons_to_str)}")
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n"
          f"{' '.join(wagons_to_str)}")