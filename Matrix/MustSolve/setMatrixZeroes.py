
def printArr(arr):
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()

#space: O(m*n)
def setMatrixZeroesWithCopy(arr):
    m = len(arr)
    n = len(arr[0])
    # copy = [[0]*n]*m # [[0]*n]*m creates a shallow copy of the list
    copy = [[0] * n for _ in range(m)]
    print(copy)
    for i in range(m):
        for j in range(n):
            copy[i][j] = arr[i][j]
    for i in range(m):
        for j in range(n):
            if copy[i][j] == 0:
                for k in range(m):
                    arr[k][j] = 0
                for k in range(n):
                    arr[i][k] = 0
    printArr(arr)

# space: O(m+n)
def setMatrixZero(arr):
    m = len(arr)
    n = len(arr[0])
    rows = [False]*m
    cols = [False]*n
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                arr[i][j] = 0

    printArr(arr)

# space: O(1)

    




setMatrixZero([[1,1,1],[1,0,1],[1,1,1]])
print()
setMatrixZeroesWithCopy( [[0,1,2,0],[3,4,5,2],[1,3,1,5]] )

# [[1,0,1],[0,0,0],[1,0,1]]

