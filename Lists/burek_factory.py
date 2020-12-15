energy = 100
coins = 100
events = input()
events_list = events.split("|")
isDayOver = True
for each in range(0, len(events_list)):
    event = events_list[each].split("-")
    if event[0] == "rest":
        if energy >= 100:
            print(f"You gained 0 energy.")
            energy = 100
            print('Current energy: 100.')
        elif (100-energy) + int(event[1]) > 100:
            energy = 100
            print(f'You gained {(100-energy)} energy.')
            print('Current energy: 100.')
        else:
            energy+=int(event[1])
            print(f'You gained {event[1]} energy.')
            print(f'Current energy: {energy}.')
    elif event[0] == "order":

        if energy - 30 >= 0:
            coins += int(event[1])
            print(f'You earned {event[1]} coins.')
            energy -= 30
        else:
            energy += 50
            print(f'You had to rest!')
    elif not event[0] == "rest" or event[0] == "order":
        coins -= int(event[1])
        if coins > 0:
            print(f'You bought {event[0]}.')
        else:
            print(f'Closed! Cannot afford {event[0]}.')
            isDayOver = False
            break
if isDayOver:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')