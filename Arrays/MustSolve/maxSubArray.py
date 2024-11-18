def maxSubArray(nums):
    # Kadane's Algorithm
    max_sum = 0
    sum = 0
    for i in range(len(nums)):
        if sum < 0:
            sum = 0
        sum += nums[i]
        max_sum = max(sum,max_sum)

    return max_sum





print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6