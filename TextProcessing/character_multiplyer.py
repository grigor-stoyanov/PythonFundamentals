line = input().split()
long = line[0]
short = line[1]
result = 0
if len(short) > len(long):
    short, long = long, short
for i in range(0, len(long)):
    if i in range(0, len(short)):
        result += ord(short[i]) * ord(long[i])
    else:
        result += ord(long[i])
print(result)
