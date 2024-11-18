def twoSums(nums, target):
    prevMap = {} # value -> index
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[nums[i]] = i

    

nums = [2, 7, 11, 15]
target = 17
print(twoSums(nums, target)) # [0, 1]
    