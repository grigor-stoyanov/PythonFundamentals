def product_is_negative(a, b, c):
    arr = [a, b, c]
    count = 0
    isnull = False
    for i in range(0, 3):
        if arr[i] < 0:
            count += 1
        elif arr[i] == 0:
            isnull == True
            break
    if count % 2 == 1 and not isnull:
        print("negative")
    elif isnull:
        print("zero")
    else:
        print("positive")


num1 = int(input())
num2 = int(input())
num3 = int(input())
product_is_negative(num1, num2, num3)
