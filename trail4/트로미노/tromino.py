n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_stair(x, y):
    tot = grid[x][y] + grid[x + 1][y] + grid[x][y + 1] + grid[x+ 1][y + 1]

    return tot - min(grid[x][y], grid[x + 1][y], grid[x][y + 1], grid[x+ 1][y + 1])

def get_row(x, y):
    return grid[x][y] + grid[x + 1][y] + grid[x + 2][y]

def get_col(x, y):
    return grid[x][y] + grid[x][y + 1] + grid[x][y + 2]

max_val = 0

for i in range(n):
    for j in range(m):
        if i + 1 < n and j + 1 < m:
            max_val = max(max_val, get_stair(i, j))
        if i + 2 < n:
            max_val = max(max_val, get_row(i, j))
        if j + 2 < m:
            max_val = max(max_val, get_col(i, j))
        
print(max_val)
