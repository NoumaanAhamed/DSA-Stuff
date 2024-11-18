def printAllCombinations(n,k):
    res = []
    def helper(n, k, index, slate):
        if len(slate) == k:
            res.append(slate.copy())
        else:
            for i in range(index, n+1):
                slate.append(i)
                helper(n, k, i+1, slate)
                slate.pop()
    helper(n, k, 1, [])
    return res
print(printAllCombinations(4,2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

