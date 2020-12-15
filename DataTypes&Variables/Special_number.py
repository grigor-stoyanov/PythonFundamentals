# #sum 5 7 or 11
# n = int(input())
# sum_digits = 0
# for i in range(1,n+1):
#     digits = i
#     while not digits == 0:
#         digit = int(digits % 10)
#         digits = int(digits/10)
#         sum_digits += digit
#     if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
#         print(f'{i} -> True')
#     else:
#         print(f'{i} -> False')
#     sum_digits = 0
n = int(input())
sum = 0
for i in range(1,n+1):
    result = 0
    num = str(i)
    for char in num:
        sum += int(char)
        if sum == 5 or sum == 7 or sum == 11:
            print(f'{i} -> True')
        else:
            print(f'{i} -> False')
        sum = 0
