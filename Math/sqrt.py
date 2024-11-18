def squareRoot(num):
    if num < 0:
        return -1
    if num == 0 or num == 1:
        return num
    start = 1
    end = num
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == num:
            return mid
        if mid * mid < num:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

print(squareRoot(16)) # 4