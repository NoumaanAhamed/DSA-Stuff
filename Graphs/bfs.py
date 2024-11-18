from collections import deque
import queue

def bfs(matrix):
    # Check for an empty matrix/graph.
    if not matrix:
        return []

    islands = 0
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        queue = deque()
        visited.add((i,j))
        queue.append((i,j))
        while queue:
            print(f"Current Queue: {queue}")
            curr_i, curr_j = queue.popleft()
            # if (curr_i, curr_j) not in visited:
            # visited.add((curr_i, curr_j))
            # print(f"Visited node: ({curr_i}, {curr_j})")
            # Traverse neighbors.
            for dr,dc in directions:
                r,c = i + dr, j + dc
                if (r in range(rows) and c in range(cols) and (r,c) not in visited and matrix[r][c] == 1):
                    # Add in question-specific checks, where relevant.
                    queue.append((r,c))
                    visited.add((r,c))
    for i in range(rows):
        for j in range(cols):
            print("--------------------")
            if matrix[i][j] == 1 and (i,j) not in visited:
                traverse(i, j)
                islands += 1

    return islands
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

# Start BFS traversal from node 0
visited_nodes = bfs(matrix)

print("Visited nodes in BFS order:", visited_nodes)