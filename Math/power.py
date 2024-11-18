# implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    
    return x * power(x, n - 1)

print(power(2, 10)) # 1024