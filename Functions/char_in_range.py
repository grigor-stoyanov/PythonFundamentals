def between(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


char1 = input()
char2 = input()
between(char1, char2)