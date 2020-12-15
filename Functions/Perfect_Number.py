def is_perfect(number):
    if number > 10:
        new_number = number
    else:
        new_number = 0
    sum_number = 0
    while len(str(new_number)) != 1:
        i = 0
        while i < len(str(new_number)):
            sum_number += int(str(new_number)[i])
            i += 1
        new_number = sum_number
        sum_number = 0

    if number == 6 or new_number == 1 and number % 10 != 0 and number % 2 == 0:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


num = int(input())
is_perfect(num)

#
# def is_perfect(number)

# sum_numbers = number//4 + 1
#     for i in range(2, (number // 4)):
#         if number % i == 0:
#             sum_numbers += i
#     if sum_numbers * 2 == number:
#         print('We have a perfect number!')
#     else:
#         print('It\'s not so perfect.')
#
#
# num = int(input())
# is_perfect(num)
