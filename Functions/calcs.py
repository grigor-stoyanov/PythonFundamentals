def calc(func, a, b):
    if func == 'multiply':
        return print(a * b)
    elif func == 'divide' and b != 0:
        return print(int(a / b))
    elif func == 'add':
        return print(a + b)
    elif func == 'subtract':
        return print(a - b)


operation = input()
num1 = int(input())
num2 = int(input())
calc(operation, num1, num2)
