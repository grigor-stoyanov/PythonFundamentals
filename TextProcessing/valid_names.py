line = input().split(', ')
condition1 = False
condition2 = False
for ele in line:
    if 3 <= len(ele) <= 16:
        condition1 = True
    else:
        continue
    for ch in ele:
        if ch.isalnum() or ch in '-_':
            condition2 = True
        else:
            condition2 = False
            break
    if condition1 and condition2:
        print(ele)
