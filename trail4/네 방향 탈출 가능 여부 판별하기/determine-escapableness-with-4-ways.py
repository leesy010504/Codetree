from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque([(0, 0)])
result = 0

while q:
    r, c = q.popleft()

    if r == n - 1 and c == m - 1:
        result = 1
        break
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if a[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc))

print(result)