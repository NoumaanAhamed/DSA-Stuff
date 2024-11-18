def bestTimeToBuyAndSellStock(arr):
    # i,j = 0,1
    # ans = 0
    # while (j < len(arr)):
    #     if(arr[i] < arr[j]):
    #         ans = max(ans,arr[j]-arr[i])
    #     else:
    #         i+=1
    #     j+=1
    # return ans
    buy = arr[0]
    profit = 0
    max_profit = 0
    for i in range(1,len(arr)):
        if(arr[i] < buy ):
            buy = min(buy,arr[i])
        else:
            profit = arr[i] - buy
            max_profit = max(profit,max_profit)
    return max_profit



print(bestTimeToBuyAndSellStock([7,1,5,3,6,4])) # 5