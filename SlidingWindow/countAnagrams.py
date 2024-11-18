def countOccurencesOfAnagrams(s, p):
    n = len(s)
    m = len(p)
    count = 0
    p = sorted(p)
    for i in range(n-m+1):
        if sorted(s[i:i+m]) == p:
            count += 1
    return count

s = "forxxorfxdofr"
p = "for"
print(countOccurencesOfAnagrams(s, p)) # 3