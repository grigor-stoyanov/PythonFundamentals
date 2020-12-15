factor = int(input())
count = int(input())
result = count
#2 4 6 8 10 count 2 factor 5
a = []
for i in range(0, factor):
    a.append(result)
    result += count
print(a)