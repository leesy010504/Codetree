n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[False] * n for _ in range(n)]

q = []
for r, c in starts:
    r, c = r - 1, c - 1
    if not visited[r][c]:
        visited[r][c] = True
        q.append((r, c))

head = 0
while head < len(q):
    r, c = q[head]
    head += 1
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
            visited[nr][nc] = True
            q.append((nr, nc))

print(len(q))