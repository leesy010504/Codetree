from itertools import combinations
from collections import deque

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

stones = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

def bfs():
    seen = [[False] * n for _ in range(n)]
    dq = deque()
    for i in range(k):
        seen[r[i]][c[i]] = True
        dq.append((r[i], c[i]))
    cnt = k
    while dq:
        x, y = dq.popleft()
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny] and grid[nx][ny] == 0:
                seen[nx][ny] = True
                cnt += 1
                dq.append((nx, ny))
    return cnt

best = 0
for comb in combinations(stones, m):
    for x, y in comb:
        grid[x][y] = 0
    best = max(best, bfs())
    for x, y in comb:
        grid[x][y] = 1
print(best)