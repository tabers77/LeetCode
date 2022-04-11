# Hints: Use BFS (this is an iterative algorithm)
import collections


def numIslands(grid):

    if not grid:
        return 0
    # Get the dimension of the grid (n_rows and n_cols)
    rows, cols = len(grid), len(grid[0])
    visit = set()
    n_islands = 0

    def bfs(r, c):
        q = collections.deque()
        q.append((r, c))
        visit.add((r, c))

        # While q is not empty we will keep appending or island
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visit:
                bfs(r, c)
                n_islands += 1

    return n_islands


grid =[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))