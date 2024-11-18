def binarySearchInReverse(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # Check if x is present at mid
        if arr[mid] > x:
            low = mid + 1
        # If x is greater, ignore left half
        elif arr[mid] < x:
            high = mid - 1
        # If x is smaller, ignore right half
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

# Test
arr = [40,10,5,4,3,2,1]
print(binarySearchInReverse(arr, 1)) # 3

#note

# write mid = (high + low) // 2 as mid = low + (high - low) // 2 to avoid overflow