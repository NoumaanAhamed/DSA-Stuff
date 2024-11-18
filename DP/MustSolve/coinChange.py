# brute force
def coinChange(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    res = float('inf')
    for coin in coins:
        sub_res = coinChange(coins, amount - coin)
        if sub_res >= 0:
            res = min(res, sub_res + 1)
    return res if res != float('inf') else -1

# brute force with memoization
def coinChangeWithMemo(coins, amount):
    memo = {}
    def helper(amount):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = float('inf')
        for coin in coins:
            sub_res = helper(amount - coin)
            if sub_res >= 0:
                print("sub-res",sub_res)
                res = min(res, sub_res + 1)
        memo[amount] = res if res != float('inf') else -1
        return memo[amount]
    return helper(amount)

# using bottom up approach
def coinChangeBottomUp(coins, amount):
    memo = {}
    memo[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                memo[i] = min(memo.get(i, float('inf')), memo[i - coin] + 1)
    return memo.get(amount, -1)


coins = [1, 2, 5]
amount = 11
# print(coinChange(coins, amount)) # 3
# print(coinChangeWithMemo(coins, amount)) # 3
print(coinChangeBottomUp(coins, amount)) # 3