from collections import deque


def matrix01(mat):
    m, n = len(mat), len(mat[0])
    q = deque()
    seen = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
                seen[i][j] = True
    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and not seen[nr][nc]:
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
                seen[nr][nc] = True

    return mat

def matrix01AlongWithPrintStatements(mat):
    m, n = len(mat), len(mat[0])
    q = deque()
    seen = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
                seen[i][j] = True
    while q:
        r, c = q.popleft()
        print(f"->r: {r}, c: {c}")
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r+dr, c+dc
            print(f"nr: {nr}, nc: {nc}")
            if 0 <= nr < m and 0 <= nc < n and not seen[nr][nc]:
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
                seen[nr][nc] = True
                print(f"mat[nr][nc]: {mat[nr][nc]}")
                print(f"q: {q}")
                print(f"seen: {seen}")
                print("------")

    return mat

mat = [[0,0,0],[0,1,0],[1,1,1]]
res = matrix01(mat)
print(res) # [[0,0,0],[0,1,0],[1,2,1]]
res = matrix01AlongWithPrintStatements(mat)
print(res) # [[0,0,0],[0,1,0],[1,2,1]]