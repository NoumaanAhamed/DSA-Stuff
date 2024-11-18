def graphDfs(mat):
    n = len(mat)
    visited = [False]*n
    def dfs(node):
        print(node, end=" ")
        visited[node] = True
        for i in range(n):
            if mat[node][i] and not visited[i]:
                dfs(i)
    for i in range(n):
        if not visited[i]:
            dfs(i)
    print()
    return


res = graphDfs([[0,1,1,0],
                [1,0,0,1],
                [1,0,0,1],
                [0,1,1,0]])
print(res) # 0 1 2 3