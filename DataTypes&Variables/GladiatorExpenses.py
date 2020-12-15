lost = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armour = float(input())
cost = 0
counter = 0
for i in range(1,lost+1):
    if i%2 == 0:
       cost += helmet
    if i%3 == 0:
        cost += sword
    if i%6 == 0:
        cost += shield
        counter += 1
    if counter == 2:
        cost += armour
        counter = 0
print("Gladiator expenses: {:.2f} aureus".format(cost))