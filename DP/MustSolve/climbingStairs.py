#dfs approach
def climbingsStairs(n):
    memo = {}
    def dfs(n):
        if n in memo:
            return memo[n]
        if n <= 2:
            return n
        memo[n] = dfs(n - 1) + dfs(n - 2)
        return memo[n]
    return dfs(n)




print(climbingsStairs(3)) # 3
