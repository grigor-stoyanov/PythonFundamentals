nums = input().split()
for _ in range(len(nums)):
    nums[_] = int(nums[_])
k = int(input())
mutation = []
i = 0
while len(nums) > 0:
    i = (i-1+k) % len(nums)
    mutation.append(nums.pop(i))
print('['+','.join([str(mutation[j]) for j in range(len(mutation))])+']')