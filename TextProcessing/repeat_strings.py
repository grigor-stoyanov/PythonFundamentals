# line = input().split()
# for ele in line:
#     for i in range(0, len(ele)):
#         print(ele, end='')
def repeat(word, constant, times):
    if len(word) == len(times * constant):
        return word
    else:
        return repeat(word + constant, constant, times)


line = input().split()
new_line = []
for ele in line:
    new_line.append(repeat(ele, ele, len(ele)))
print(''.join(new_line))