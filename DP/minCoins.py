# using greedy approach
def minimumCoins(coins, amount):
    coins.sort(reverse=True)
    res = 0
    for coin in coins:
        if amount == 0:
            break
        res += amount // coin
        amount %= coin
    return res  

coins = [1, 2, 5]
amount = 11
print(minimumCoins(coins, amount)) # 3