n = int(input())
word = input()
a = []
b = []
for i in range(0, n):
    text = input()
    a.append(text)
    if word in text:
        b.append(text)
print(f'{a}\n{b}')
