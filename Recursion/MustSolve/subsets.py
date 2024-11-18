def printSubsets(nums):
    res = []
    def helper(out,inp):
        print("out:",out,',inp:',inp)
        if(len(inp) == 0):
            res.append(out)
            return
        op1 = out.copy()
        op2 = out.copy()
        print("op1:",op1,",op2:",op2,',inp:',inp)
        op2.append(inp[0])
        # inp.pop(0)
        print("op1:",op1,",op2:",op2,',inp:',inp)
        helper(op1,inp[1:])
        helper(op2,inp[1:])
    helper([],nums)
    return res

nums = [1,2,3]
print(printSubsets(nums)) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Same solution for powerset/all subsets/subsequences
# for uniqye subsets use map to remove duplicates
# for lexico-graphical order use sort

# Generate Recursive tree for the above logic
