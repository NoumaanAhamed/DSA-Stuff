def generateParenthesis(n):
    res = []
    def helper(open,close,raw_str):
        if(open == 0 and close == 0):
            res.append(raw_str)
            return
        if(open != 0):
            helper(open-1,close,raw_str+'(')
        if(close > open):
            helper(open,close-1,raw_str+')')
    helper(n,n,'')
    return res


print(generateParenthesis(3)) # ['((()))', '(()())', '(())()', '()(())', '()()()']