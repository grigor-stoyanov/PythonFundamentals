def operation(a, b):
    factorial_a = 1
    factorial_b = 1
    for i in range(2, a + 1):
        factorial_a = factorial_a * i
    for i in range(2, b+1):
        factorial_b = factorial_b * i
    result = factorial_a / factorial_b
    return result


num1 = int(input())
num2 = int(input())

print(f'{operation(num1, num2):.2f}')
