memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    elif n <= 2:
        res = 1
    else:
        res = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = res
    return res

def fibWithoutMemo(n):
    if n <= 2:
        return 1
    return fibWithoutMemo(n - 1) + fibWithoutMemo(n - 2)

# bottom up approach
def fib(n):
    memo = {}
    for i in range(1, n + 1):
        if i <= 2:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

print(fibonacci(350))
print(fib(350))
# print(fibWithoutMemo(35)) 

# fib serires
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610