nums = input()
beggars = int(input())
nums_list = nums.split(', ')
profit = []
for i in range(beggars):
    profit.append(0)
i = 0
while len(nums_list)>0:
    nums_list[0] = int(nums_list[0])
    if i < len(profit):
        profit[i]+=nums_list[0]
    else:
        i = 0
        continue
    nums_list.pop(0)
    i+=1
print(profit)
