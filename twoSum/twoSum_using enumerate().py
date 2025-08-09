
def twoSum(nums, target):
    nummap = {}

    for i, num in enumerate(nums): 
    #emunerate is used to seperate index and values of an array

        compliment = target - num
        if compliment in nummap:
            return [nummap[compliment], i ]
        nummap[num] = i

nums = [5,6,2,4];
target = 9;

print(twoSum(nums, target))