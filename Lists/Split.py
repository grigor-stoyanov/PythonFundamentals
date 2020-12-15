text = input()
a = text.split(" ")
for i in range(0, len(a)):
    a[i] = -int(a[i])
print(a)
