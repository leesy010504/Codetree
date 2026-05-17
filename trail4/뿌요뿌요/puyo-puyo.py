n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(r, c, num):
    visited[r][c] = True
    block_size = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc] and grid[nr][nc] == num:
                block_size += dfs(nr, nc, num)
        
    return block_size


biggest_block = 0
count = 0

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            curr_block = dfs(r, c, grid[r][c])

            if biggest_block < curr_block:
                biggest_block = curr_block
            
            if curr_block >= 4:
                count += 1

print(count, biggest_block)