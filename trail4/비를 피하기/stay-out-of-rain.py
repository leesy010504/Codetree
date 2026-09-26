from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * n for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            q.append((i,j))
            dist[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] != 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    answer = []

    for j in range(n):

        if grid[i][j] == 2:
            answer.append(dist[i][j])
        else:
            answer.append(0)
    
    print(*answer)
