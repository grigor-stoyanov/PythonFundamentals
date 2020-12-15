sequence = input().split()
cmd = input()
turn = 1
a = 5
while not cmd == 'end':
    ele1, ele2 = cmd.split()
    if not (0 <= int(ele1) < len(sequence) and 0 <= int(ele2) < len(sequence)) and ele1 != ele2:
        new_ele = str(-turn) + 'a'
        sequence.insert(len(sequence) // 2, new_ele)
        sequence.insert(len(sequence) // 2, new_ele)
        print("Invalid input! Adding additional elements to the board")
        turn += 1
        cmd = input()
        continue
    if sequence[int(ele1)] == sequence[int(ele2)]:
        print(f"Congrats! You have found matching elements - {sequence[int(ele1)]}!")
        if int(ele1) > int(ele2):
            a = int(ele1)
            b = int(ele2)
        else:
            a = int(ele2)
            b = int(ele1)
        sequence.pop(a)
        sequence.pop(b)
    else:
        print("Try again!")
    if not sequence:
        print(f"You have won in {turn} turns!")
        break
    turn += 1
    cmd = input()
if sequence:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")
