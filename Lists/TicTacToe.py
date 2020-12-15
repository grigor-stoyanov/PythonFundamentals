tic_hor = input().split()
tac_hor = input().split()
toe_hor = input().split()

# [[a,b,c][a,b,c][a,b,c]] hor
hor_matrix = [tic_hor, tac_hor, toe_hor]
# [a,a,a][b,b,b][c,c,c] ver
tic_ver = [tic_hor[0], tac_hor[0], toe_hor[0]]
tac_ver = [tic_hor[1], tac_hor[1], toe_hor[1]]
toe_ver = [tic_hor[2], tac_hor[2], toe_hor[2]]
ver_matrix = [tic_ver, tac_ver, toe_ver]
# [a,b,c][a,b,c]
left_dia = [tic_hor[0], tac_hor[1], toe_hor[2]]
right_dia = [tic_hor[2], tac_hor[1], toe_hor[0]]
dia_matrix = [left_dia, right_dia]
counter1 = 0
counter2 = 0
counter_dias = 0
winner = None
for i in range(0, 3):
    for j in range(0, 3):
        if hor_matrix[i][j] == "1":
            counter1 += 1
        elif hor_matrix[i][j] == "2":
            counter2 += 1
        if j >= 1 and not (counter1 >= 1 or counter2 >= 1):
            break
        if counter1 == 3 or counter2 == 3:
            winner = counter1 > counter2
    if winner is None:
        counter1 = 0
        counter2 = 0
    else:
        break
    for k in range(0, 3):
        if ver_matrix[i][k] == "1":
            counter1 += 1
        elif ver_matrix[i][k] == "2":
            counter2 += 1
        if k >= 1 and not (counter1 >= 1 or counter2 >= 1):
            break
        if counter1 == 3 or counter2 == 3:
            winner = counter1 > counter2
    if winner is None:
        counter1 = 0
        counter2 = 0
    else:
        break
    if not counter_dias >= 2:
        counter_dias += 1
        for m in range(0, 3):
            if dia_matrix[i][m] == "1":
                counter1 += 1
            elif dia_matrix[i][m] == "2":
                counter2 += 1
            if m >= 1 and not (counter1 >= 1 or counter2 >= 1):
                break
            if counter1 == 3 or counter2 == 3:
                winner = counter1 > counter2
    if winner is None:
        counter1 = 0
        counter2 = 0
    else:
        break
if winner is None:
    print("Draw!")
elif winner:
    print("First player won")
elif not winner:
    print("Second player won")
