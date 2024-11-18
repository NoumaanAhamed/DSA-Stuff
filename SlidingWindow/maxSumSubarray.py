# sliding window code 
# Q) Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

def maxSum(arr, k):
    i,j = 0,0
    curr = 0
    max_sum = 0
    while(j < len(arr)):
        curr += arr[j]
        if(j-i+1 < k):
            j+=1
        elif(j-i+1 == k):
            max_sum = max(curr,max_sum)
            curr -= arr[i]
            j+=1
            i+=1
    return max_sum

# test cases
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(maxSum(arr,k)) # 9

arr = [2, 3, 4, 1, 5]
k = 2
print(maxSum(arr,k)) # 7

arr = [2, 1, 5, 2, 8]
k = 4
print(maxSum(arr,k)) # 17

arr = [3, 4, 1, 1, 6]
k = 3
print(maxSum(arr,k)) # 8

arr = [1, 3, 2, 6, 4]
k = 3
print(maxSum(arr,k)) # 12
