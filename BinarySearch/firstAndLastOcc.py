def firstAndLastOcc(arr, n, x):
    i,j = 0,n-1
    first,last = 0,0
    while(i <= j):
        mid = (i+j)//2
        if(arr[mid] == x):
            i,j = mid,mid
            while(i!=0 and arr[i-1] == x):
                print("in i",i,arr[i])
                i -= 1
            while(j!=n-1 and arr[j+1] == x):
                print("in j",j,arr[j])
                j += 1
            return [i,j]
        elif(arr[mid] > x):
            j = mid -1
        else:
            i = mid+1
    return [-1,-1]

print(firstAndLastOcc([1, 3, 5, 5, 5, 5, 67, 123, 125], 9, 5)) # (2, 5)