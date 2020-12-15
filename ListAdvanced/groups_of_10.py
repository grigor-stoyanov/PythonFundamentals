def filter_group(arr, index):
    arr = [each for each in arr if each // (10 * index) == 0 or (each // 10 == index and each % 10 == 0)]
    return arr


list_of_nums = [int(ele) for ele in input().split(', ')]
i = 1
while not len(list_of_nums) == 0:
    current_group = filter_group(list_of_nums, i)
    print(f'Group of {i * 10}\'s: {current_group}')
    i += 1
    list_of_nums = [ele for ele in list_of_nums if ele not in current_group]
