# sum of two numbers without using + or - operator
def sum(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(sum(5, 7)) # 12

#dry run
# 5 = 101
# 7 = 111

