def longestSubstringNoRepeatingChar(s):
    i,j,count = 0,0,0
    sMap = {}
    while(j < len(s)):
        if s[j] in sMap:
            sMap[s[j]] += 1
        else:
            sMap[s[j]] = 1
        if(len(sMap) == j-i+1):
            count = max(count,j-i+1)
            j+=1
        else:
            while len(sMap) < j-i+1:
                sMap[s[i]] -= 1
                if(sMap[s[i]] == 0):
                    del sMap[s[i]]
                i+=1
            j+=1
    return count


s = "pwwkew"
print(longestSubstringNoRepeatingChar(s)) # 3