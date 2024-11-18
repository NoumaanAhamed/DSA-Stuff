from collections import deque

def dfs(image, sr, sc, newColor, oldColor):
    if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != oldColor:
        return
    image[sr][sc] = newColor
    dfs(image, sr+1, sc, newColor, oldColor)
    dfs(image, sr-1, sc, newColor, oldColor)
    dfs(image, sr, sc+1, newColor, oldColor)
    dfs(image, sr, sc-1, newColor, oldColor)

def bfs(image, sr, sc, newColor, oldColor):
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != oldColor:
            continue
        image[r][c] = newColor
        q.append((r+1, c))
        q.append((r-1, c))
        q.append((r, c+1))
        q.append((r, c-1))

def floodFill(image, sr, sc, newColor):
    oldColor = image[sr][sc]
    if oldColor != newColor:
        bfs(image, sr, sc, newColor, oldColor)
    return image


# test cases

# 1
print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)) 
# 2
print(floodFill([[0,0,0],[0,1,1]], 1, 1, 1)) 
# 3
print(floodFill([[0,0,0],[0,1,1]], 0, 1, 1)) 
# 4
print(floodFill([[0,0,0],[0,1,1]], 1, 1, 2))
# 5
print(floodFill([[0,0,0],[0,1,1]], 1, 1, 0))