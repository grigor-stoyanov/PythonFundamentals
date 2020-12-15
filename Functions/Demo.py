# # Параметри
# def custom_split(text, separator):
#     result = text.split(separator)
#     return result
#
#
# # Аргументи
# print(custom_split("Hello;there", ";"))
#
# # default аргументи
# def default_arguments(firstname='Genadi', lastname='Dimitrov'):
#     print(firstname,lastname)
# default_arguments()
# # named аргументи
# def named_argument(firstname,lastname):
#     print(firstname,lastname)
# named_argument(firstname='Ines',lastname='Ivanova')

# рекурсия
def factorial(x):
    # """This is a recursive function
    # to find the factorial of an integer"""
    # etners own function 3 times until last one calculates final and saves number
    b = 0
    if x == 1:
        return 1
    else:
        b = (x * factorial(x-1))
        return b

num = 3
print("The factorial of", num, "is", factorial(num))