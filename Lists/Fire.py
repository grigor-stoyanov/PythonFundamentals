fires = input()
water = int(input())
fires_and_values = fires.split('#')
# fires_andvalues = input().split('#')
effort = 0
total_fire = 0
print("Cells:")
# 1250 {High = 89,Low = 28,Medium = 77,Low = 23}
# cycle trough list
# split every element and check validity
# if valid put out and substract water/calculate effort
# print cells in order until no water left
# print effort and total fire put out
# for fire in fires_and values:
#   fire, value = fire.split(" = ")
for i in range(0, len(fires_and_values)):
    fire_cell = fires_and_values[i].split(" = ")
# {High,89}
    if fire_cell[0] == 'High' and not (81 <= int(fire_cell[1]) <= 125):
# RANGE_HIGH == range(80,126) константи в главани букви
# if fire == 'High' and not value in range_high
        continue
    elif fire_cell[0] == 'Medium' and not (51 <= int(fire_cell[1]) <= 80):
        continue
    elif fire_cell[0] == 'Low' and not (1 <= int(fire_cell[1]) <= 50):
        continue
    if water >= int(fire_cell[1]):
        water -= int(fire_cell[1])
        total_fire += int(fire_cell[1])
        effort += 0.25 * int(fire_cell[1])
        print(f' - {int(fire_cell[1])}')
    else:
        continue
    if water <= 0:
        break
print(f'Effort: {effort:.2f}\nTotal Fire: {total_fire}')
