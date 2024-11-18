def validAnagram(s,t):
    if(len(s) != len(t)):
        return False
    map = {}
    map1 = {}
    for i in range(len(s)):
        if s[i] in map:
            map[s[i]]+=1
        else:
            map[s[i]] = 1
    for i in range(len(s)):
        if t[i] in map1:
            map1[t[i]]+=1
        else:
            map1[t[i]] = 1
    
    return map == map1

# or use sorted(s) 

print(validAnagram("anagram","nagaram"))