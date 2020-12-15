number_of_wagons = int(input())
wagons = [0 for _ in range(number_of_wagons)]
cmd = input()
while not cmd == "end":
    data = cmd.split()
    if data[0] == "add":
        number_of_people = int(data[1])
        wagons[-1] += number_of_people
    elif data[0] == "insert":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += number_of_people
    elif data[0] == "leave":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people
    cmd = input()
print(wagons)