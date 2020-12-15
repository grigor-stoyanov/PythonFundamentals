num_line = input().split(',')
num_line = [int(num_line[i]) for i in range(len(num_line))]
index = 0
num_index = list(filter(lambda index: num_line[index] % 2 == 0, range(index, len(num_line))))
print(num_index)
