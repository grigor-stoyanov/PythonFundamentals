n = int(input())
rows = []
temp = []
cols = []
i = 0
while i < n:
    rows.append(input().split())
    i += 1
for j in range(0, len(rows[0])):
    if j > 0:
        cols.append(temp.copy())
    for m in range(0, n):
        if j == 0:
            temp.append(rows[m][j])
        else:
            temp[m] = rows[m][j]
cols.append(temp.copy())
cmd = input().split()
for each in range(0,len(cmd)):
    row, col = int(cmd.split("-"))
    if int(rows[row][col]) > 0:
        rows[row][col] = int(rows[row][col])-1
    else:
        continue
for _ in range(0, n):
    for f in range(0, len(row[0])):
        print(rows[f])