def longestKUniqueSubstrings(s, k):
    i,j,count = 0,0,0
    unique = {}
    while(j < len(s)):
        if s[j] in unique:
            unique[s[j]] += 1
        else:
            unique[s[j]] = 1
        # print("unique",unique)
        if(len(unique) < k):
            j+=1
        elif(len(unique) == k):
            count = max(count,j-i+1)
            j+=1
        
        else:
            while(len(unique) > k):
                unique[s[i]] -= 1
                if(unique[s[i]] == 0):
                    del unique[s[i]]
                i+=1
            j+=1
                
    return count

print(longestKUniqueSubstrings("aabacbebebe", 3)) # 7