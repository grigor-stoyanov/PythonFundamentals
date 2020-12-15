def exchange(nums_list, index):
    if 0 <= index <= len(nums_list):
        second_half = nums_list[index + 1:]
        first_half = nums_list[:index + 1]
        exchange_result = second_half + first_half
        return exchange_result
    else:
        print("Invalid index")
        return nums_list


def get_max_odd(nums_list):
    filter_only_odds = []
    for element in nums_list:
        if element % 2 == 1:
            filter_only_odds.append(element)
    if filter_only_odds:
        max_odd = max(filter_only_odds)
        for index in range(len(nums_list) - 1, -1, -1):
            if max_odd == nums_list[index]:
                break
        return index
    else:
        return "No matches"


def get_max_even(nums_list):
    filter_only_even = []
    for element in nums_list:
        if element % 2 == 0:
            filter_only_even.append(element)
    if filter_only_even:
        max_even = max(filter_only_even)
        for index in range(len(nums_list) - 1, -1, -1):
            if max_even == nums_list[index]:
                break
        return index
    else:
        return "No matches"


def get_min_odd(nums_list):
    filter_only_odd = []
    for element in nums_list:
        if element % 2 == 1:
            filter_only_odd.append(element)
    if filter_only_odd:
        min_odd = min(filter_only_odd)
        for index in range(len(nums_list) - 1, -1, -1):
            if min_odd == nums_list[index]:
                break
        return index
    else:
        return "No matches"


def get_min_even(nums_list):
    filter_only_even = []
    for element in nums_list:
        if element % 2 == 0:
            filter_only_even.append(element)
    if filter_only_even:
        min_even = min(filter_only_even)
        for index in range(len(nums_list)-1, -1, -1):
            if min_even == nums_list[index]:
                break
        return index
    else:
        return "No matches"


def get_first_even(nums_list, count):
    if count <= len(nums_list):
        filter_only_even = []
        first_count_even = []
        for element in nums_list:
            if element % 2 == 0:
                filter_only_even.append(element)
        for index in range(0, len(filter_only_even)):
            first_count_even.append(filter_only_even[index])
            count -= 1
            if count <= 0:
                break
        return first_count_even
    else:
        return "Invalid count"


def get_first_odd(nums_list, count):
    if count <= len(nums_list):
        filter_only_odd = []
        first_count_odd = []
        for element in nums_list:
            if element % 2 == 1:
                filter_only_odd.append(element)
        for index in range(0, len(filter_only_odd)):
            first_count_odd.append(filter_only_odd[index])
            count -= 1
            if count <= 0:
                break
        return first_count_odd
    else:
        return "Invalid count"


def get_last_even(nums_list, count):
    if count <= len(nums_list):
        filter_only_even = []
        last_count_even = []
        for element in nums_list:
            if element % 2 == 0:
                filter_only_even.append(element)
        for index in range(0, len(filter_only_even)):
            last_count_even.append(filter_only_even[index])
            count -= 1
            if count <= 0:
                break
        return last_count_even
    else:
        return "Invalid count"


def get_last_odd(nums_list, count):
    if count <= len(nums_list):
        filter_only_odd = []
        last_count_odd = []
        for element in nums_list:
            if element % 2 == 1:
                filter_only_odd.append(element)
        for index in range(0, len(filter_only_odd)):
            last_count_odd.append(filter_only_odd[index])
            count -= 1
            if count <= 0:
                break
        return last_count_odd
    else:
        return "Invalid count"


numbers_list = [int(i) for i in input().split()]
commands = input()
while not commands == "end":
    command = commands.split()
    if command[0] == "exchange":
        numbers_list = exchange(numbers_list, int(command[1]))
    elif command[0] == "max" and command[1] == 'odd':
        print(get_max_odd(numbers_list))
    elif command[0] == "max" and command[1] == 'even':
        print(get_max_even(numbers_list))
    elif command[0] == "min" and command[1] == 'odd':
        print(get_min_odd(numbers_list))
    elif command[0] == "min" and command[1] == 'even':
        print(get_min_even(numbers_list))
    elif command[0] == "first" and command[2] == 'even':
        print(get_first_even(numbers_list, int(command[1])))
    elif command[0] == 'first' and command[2] == 'odd':
        print(get_first_odd(numbers_list, int(command[1])))
    elif command[0] == 'last' and command[2] == 'even':
        print(get_last_even(numbers_list, int(command[1])))
    elif command[0] == 'last' and command[2] == 'odd':
        print(get_last_odd(numbers_list, int(command[1])))
    commands = input()
print(numbers_list)
