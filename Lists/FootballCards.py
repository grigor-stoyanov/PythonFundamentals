cards = input()
data = cards.split()
countA = 0
countB = 0
cardA = []
cardB = []
isTerminated = False
for i in range(len(data)):
    if data[i][0] == "A" and not data[i] in cardA:
        countA += 1
        cardA.append(data[i])
        cardB.append(0)
    elif data[i][0] == "B" and not data[i] in cardB:
        countB += 1
        cardB.append(data[i])
    if countA >= 5 or countB >= 5:
        isTerminated = True
        break;
print(f"Team A - {11 - countA}; Team B - {11 - countB}")
if isTerminated:
    print("Game was terminated")
