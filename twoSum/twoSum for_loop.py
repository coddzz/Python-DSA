nums = [5,4,11,18]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i]+nums[j] == target:
            print(i, j)
        

