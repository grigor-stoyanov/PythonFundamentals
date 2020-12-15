line = [ele.lower() for ele in input().split()]
my_dict = {}
for ele in line:
    if ele not in my_dict:
        my_dict[ele] = 1
    else:
        my_dict[ele] += 1
for key in my_dict:
    if not my_dict[key] % 2 == 0:
        print(key, end=' ')
# for word in line:
#   my_dict[word] = line.count(words)