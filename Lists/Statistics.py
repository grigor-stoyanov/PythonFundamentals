n = int(input())
pos = []
neg = []
for i in range(0, n):
    num = int(input())
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)
print(pos)
print(neg)
print(f'Count of positives: {len(pos)}. Sum of negatives: {sum(neg)}')


