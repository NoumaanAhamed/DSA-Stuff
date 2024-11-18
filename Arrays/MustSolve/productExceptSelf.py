def productExceptSelf(arr):
    # ans = []
    # count = 1
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #        if(i != j):
    #            count *= arr[j]
    #     ans.append(count)
    #     count = 1

    # return ans
    l_arr = [1] * len(arr)
    r_arr = [1] * len(arr)
    for i in range(1,len(arr)):
        l_arr[i] = l_arr[i-1] * arr[i-1]

    for i in range(len(arr) - 2,-1,-1):
        r_arr[i] = r_arr[i+1] * arr[i+1]
    
    for i in range(len(arr)):
        arr[i] = l_arr[i] * r_arr[i]

    return arr

        

print(productExceptSelf( [1,2,3,4] )) # [24,12,8,6]