lift_clients = int(input())
lift_wagons = [int(wagon) for wagon in input().split()]
index = 0
if len(lift_wagons)*4 >= lift_clients+sum(lift_wagons):
    while lift_clients != 0:
        if lift_wagons[index] < 4:
            lift_clients = (lift_wagons[index] + lift_clients) - 4
            if lift_clients >= 0:
                lift_wagons[index] = 4
            else:
                lift_wagons[index] += (lift_clients + 4)
                break
        index += 1
    if sum(lift_wagons) % 4 != 0 or lift_wagons[-1] == 0:
        print('The lift has empty spots!')
else:
    lift_clients += sum(lift_wagons)
    lift_wagons = [4 for wagon in lift_wagons]
    print(f'There isn\'t enough space! {lift_clients-sum(lift_wagons)} people in a queue!')
print(*lift_wagons)