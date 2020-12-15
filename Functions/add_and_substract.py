def add_and_subtract(a, b, c):
    def sum_numbers():
        sums = a + b
        return sums

    def sub_numbers():
        sub = sum_numbers() - c
        return sub
    sum_numbers()
    result = sub_numbers()
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
