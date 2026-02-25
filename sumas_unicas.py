nums = [0, 2, 4, 6]  

sums = set()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        sums.add(nums[i] + nums[j])

print(list(sums))
