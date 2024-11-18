def firstNegativeNum(arr,k):
    i, j = 0, 0
    num = []
    res = []
    while j < len(arr):
        if arr[j] < 0:
            num.append(arr[j])
        if j-i+1 < k:
            j += 1
        elif j-i+1 == k:
            print("num", num, "i", i, "j", j, "res", res)
            if len(num) == 0:
                res.append(0)
            else:
                res.append(num[0])
                if num[0] == arr[i]:
                    num.pop(0)
            i += 1
            j += 1
    return res

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(firstNegativeNum(arr, k)) # [-1, -7, -15, -15, -15]