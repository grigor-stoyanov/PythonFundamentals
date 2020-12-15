import math
party = int(input())
days = int(input())
coins = 0
for i in range(1,days+1):
    if i%10 == 0:
        party -= 2
    if i%15 == 0:
        party += 5
    coins += 50
    coins -= 2 * party
    if i%3 == 0:
        coins -= 3 * party
    if i%5 == 0:
        coins += 20 * party
    if i%15 == 0:
        coins -= 2 * party
coins = math.floor(coins/party)
print(f'{party} companions received {coins} coins each.')