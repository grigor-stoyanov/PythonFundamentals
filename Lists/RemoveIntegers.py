nums = input()
nums_list=[]
for i in range(0,len(nums.split())):
    nums_list.append(int(nums.split()[i]))
n = int(input())
for i in range(0, n):
    nums_list.remove(min(nums_list))
print(nums_list)