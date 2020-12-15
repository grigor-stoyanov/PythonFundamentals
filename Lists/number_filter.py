n = int(input())
a = []
for i in range(0, n):
    num = int(input())
    a.append(num)
cmd = input()
if cmd == "even":
    for i in range(n - 1, -1, -1):
        if not a[i] % 2 == 0:
            a.remove(a[i])
elif cmd == "odd":
    for i in range(n - 1, -1, -1):
        if not a[i] % 2 == 1:
            a.remove(a[i])
elif cmd == "positive":
    for i in range(n - 1, -1, -1):
        if not a[i] >= 0:
            a.remove(a[i])
elif cmd == "negative":
    for i in range(n - 1, -1, -1):
        if not a[i] < 0:
            a.remove(a[i])
print(a)
