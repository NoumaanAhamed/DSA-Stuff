def spiralMatrix(arr):
    m,n = len(arr),len(arr[0])
    top,left = 0,0
    bottom,right = m-1,n-1
    res = []
    while(top <= bottom and left <= right):

        for i in range(left,right+1):
            res.append(arr[top][i])
        top += 1

        for i in range(top,bottom+1):
            res.append(arr[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right,left-1,-1):
                res.append(arr[bottom][i])
            bottom -= 1
        
        if left<=right:
            for i in range(bottom,top-1,-1):
                res.append(arr[i][left])
            left += 1
    return res

print(spiralMatrix([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]

# [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8 ],
#     [9, 10,11,12]
# ]