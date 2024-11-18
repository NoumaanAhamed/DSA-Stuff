#using memo and recursion
def houseRobber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    memo = {}
    def dfs(i):
        if i in memo:
            return memo[i]
        if i >= len(nums):
            return 0
        memo[i] = max(dfs(i + 2) + nums[i], dfs(i + 1))
        return memo[i]
    return dfs(0)

arr = [1, 2, 3, 1]
print(houseRobber(arr)) # 4