neighbourhood = [int(each) for each in input().split('@')]
cmd = input()
houseIndex = 0
count = 0
while not cmd == 'Love!':
    jump_length = int(cmd.split()[1])
    houseIndex += jump_length
    if houseIndex >= len(neighbourhood):
        houseIndex = 0
    neighbourhood[houseIndex] -= 2
    if neighbourhood[houseIndex] == 0:
        print(f"Place {houseIndex} has Valentine's day.")
    elif neighbourhood[houseIndex] < 0:
        print(f"Place {houseIndex} already had Valentine's day.")
    cmd = input()
print(f"Cupid's last position was {houseIndex}.")
for each in neighbourhood:
    if each <= 0:
        count+=1
if count == len(neighbourhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighbourhood)-count} places.")