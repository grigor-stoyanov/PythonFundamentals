# def exchange_index(array, index):
#     if len(array)-1 > index:
#         slice1 = array[:index+1]
#         slice2 = array[index+1:]
#         slice2.extend(slice1)
#         return slice2
#     elif index > len(array) - 1:
#         return print("Invalid index")
#
#
# def max_oddfunc(array):
#     max_odd = min(array)
#     index_max_odd = None
#     for i in range(0, len(array)):
#         if array[i] % 2 == 1 and array[i] >= max_odd:
#             index_max_odd = i
#             max_odd = array[i]
#     if index_max_odd is not None:
#         return index_max_odd
#     else:
#         return "No matches"
#
#
# def max_evenfunc(array):
#     max_even = min(array)
#     index_max_even = None
#     for i in range(0, len(array)):
#         if array[i] % 2 == 0 and array[i] >= max_even:
#             index_max_even = i
#             max_even = array[i]
#     if not index_max_even is None:
#         return index_max_even
#     else:
#         return "No matches"
#
#
# def min_evenfunc(array):
#     min_even = max(array)
#     index_min_even = None
#     for i in range(0, len(array)):
#         if array[i] % 2 == 0 and array[i] <= min_even:
#             index_min_even = i
#             min_even = array[i]
#     if not index_min_even is None:
#         return index_min_even
#     else:
#         return "No matches"
#
#
# def min_oddfunc(array):
#     min_odd = max(array)
#     index_min_odd = None
#     for i in range(0, len(array)):
#         if array[i] % 2 == 1 and array[i] <= min_odd:
#             index_min_odd = i
#             min_odd = array[i]
#     if not index_min_odd is None:
#         return index_min_odd
#     else:
#         return "No matches"
#
#
# def first_count_even(array, count):
#     even = []
#     cnt_even = count
#     if not count > len(array):
#         for i in range(0, len(array)):
#             if array[i] % 2 == 0 and cnt_even > 0:
#                 even.append(array[i])
#                 cnt_even -= 1
#                 if cnt_even <= 0:
#                     break
#         return even
#     else:
#         return "Invalid count"
#
#
# def first_count_odd(array, count):
#     odd = []
#     cnt_odd = count
#     if not count > len(array):
#         for i in range(0, len(array)):
#             if array[i] % 2 == 1 and cnt_odd > 0:
#                 odd.append(array[i])
#                 cnt_odd -= 1
#                 if cnt_odd <= 0:
#                     break
#         return odd
#     else:
#         return "Invalid count"
#
#
# def last_count_even(array, count):
#     even = []
#     cnt_even = count
#     if not count > len(array):
#         for i in range(len(array) - 1, -1, -1):
#             if array[i] % 2 == 0 and cnt_even > 0:
#                 even.append(array[i])
#                 cnt_even -= 1
#                 if cnt_even <= 0:
#                     break
#         return even
#     else:
#         return "Invalid count"
#
#
# def last_count_odd(array, count):
#     odd = []
#     cnt_odd = count
#     if not count > len(array):
#         for i in range(len(array) - 1, -1, -1):
#             if array[i] % 2 == 1 and cnt_odd > 0:
#                 odd.append(array[i])
#                 cnt_odd -= 1
#                 if cnt_odd <= 0:
#                     break
#         return odd
#     else:
#         return "Invalid count"
#
#
# arr = [int(i) for i in input().split()]
# cmd = input()
# while not cmd == "end":
#     if cmd.split()[0] == "first" or cmd.split()[0] == "last":
#         command, specify1, specify2 = cmd.split()
#     else:
#         command,specify = cmd.split()
#     if command == "exchange":
#         isNone = exchange_index(arr, int(specify))
#         if isNone is not None:
#             arr = isNone
#     elif command == "max":
#         if specify == "even":
#             print(max_evenfunc(arr))
#         else:
#             print(max_oddfunc(arr))
#     elif command == "min":
#         if specify == "even":
#             print(min_evenfunc(arr))
#         else:
#             print(min_oddfunc(arr))
#     elif command == "first":
#         if specify2 == "odd":
#             print(first_count_odd(arr, int(specify1)))
#         else:
#             print(first_count_even(arr, int(specify1)))
#     elif command == "last":
#         if specify2 == "odd":
#             print(last_count_odd(arr, int(specify1)))
#         else:
#             print(last_count_even(arr, int(specify1)))
#     cmd = input()
# print(arr)