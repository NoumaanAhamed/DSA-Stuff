def largestSubArrayOfSumK(arr,k):
    i,j,count,sum =0,0,0,0
    while(j < len(arr)):
        sum += arr[j]
        if(sum < k):
            j+=1
        elif(sum == k):
            count = max(count,j-i+1)
            j+=1
        else:
            while(sum > k):
                sum -= arr[i]
                i+=1
            if sum == k:
                count = max(count,j-i+1)
            j+=1
    return count
        
# standard twmplate for variable slinding window

# i,j = 0,0
# ans = 0
# while(j < len(arr)):
#     # calculate
#     j+=1
#     if(condition):
#         # update answer
#     while(condition not met):
#         # shrink window
#         i+=1
#     j+=1
# return ans


