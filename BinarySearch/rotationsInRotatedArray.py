def minValInRotatedArr(arr):
    n = len(arr)
    start = 0
    end = n - 1
    
    while start <= end:
        mid = start + (end-start)//2
        prev = (mid-1+n)%n
        next = (mid+1)%n
        if(arr[mid] < arr[prev] and arr[mid] < arr[next]):
            return mid
        elif(arr[end] > arr[mid]):
            end = mid - 1
        elif(arr[mid] > arr[end]):
            start = mid + 1
    return -1

def binarySearch(arr,x):
    i,j = 0,len(arr)-1
    while(i<=j):
        mid = i + (j-i)//2
        if(arr[mid] == x):
            return mid
        elif(arr[mid] > x):
            j = mid - 1
        else:
            i = mid + 1
    return -1

def findEleInRotatedArr(arr,k):
    index = minValInRotatedArr(arr)
    arr = arr[index:] + arr[:index]
    res = binarySearch(arr,k)
    if res == -1:
        return -1
    return res + index

print(findEleInRotatedArr([4,5,6,7,0,1,2],3))

# print(binarySearch([1,2,3,4,7],7))

# print(minValInRotatedArr([11, 12, 15,15, 18, 2, 5, 6, 8,8])) # 4

