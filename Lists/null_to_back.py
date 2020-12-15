nums = input().split(", ")
for each in range(0, len(nums)):
    nums[each] = int(nums[each])
i = 1
n = len(nums)
while i < n:
    if nums[i-1] == 0:
        nums.pop(i-1)
        i -= 1
        nums.append(0)
        n -= 1
    i += 1
print(nums)