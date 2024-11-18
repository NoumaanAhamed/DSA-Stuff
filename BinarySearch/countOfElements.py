def countOfElement(arr,k):
    left = leftIndex(arr,k)
    right = rightIndex(arr,k)
    if left == -1 or right == -1:
        return 0
    return right - left + 1

def leftIndex(arr,k):
    i,j = 0,len(arr)-1
    res = -1
    while(i <= j):
        mid = (i+j)//2
        if(arr[mid] == k):
            res = mid
            j = mid - 1
        elif(arr[mid] > k):
            j = mid - 1
        else:
            i = mid + 1
    return res

def rightIndex(arr,k):
    i,j = 0,len(arr)-1
    res = -1
    while(i <= j):
        mid = (i+j)//2
        if(arr[mid] == k):
            res = mid
            i = mid + 1
        elif(arr[mid] > k):
            j = mid - 1
        else:
            i = mid + 1
    return res
    

print(countOfElement([1, 3, 5, 5, 5, 5, 67, 123, 125], 51)) # 4