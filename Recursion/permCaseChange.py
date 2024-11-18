def permutationWithCaseChange(s):
    res = []
    def helper(out,inp):
        if(len(inp) == 0):
            res.append(out)
            return
        op1 = out + inp[0].lower()
        op2 = out + inp[0].upper()
        helper(op1,inp[1:])
        helper(op2,inp[1:])
    helper("",s)
    return res


s = "a1b2"
raw_arr = permutationWithCaseChange(s)
hMap = {}
for i in raw_arr:
    hMap[i] = 1
print(list(hMap.keys()))

# Output:
# ab
# aB
# Ab
# AB
