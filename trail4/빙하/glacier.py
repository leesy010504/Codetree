from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs():
    melt_list = []
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        visited[r][c] = True
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                visited[nr][nc] = True
                if a[nr][nc] == 0:
                    q.append((nr, nc))
                else:
                    melt_list.append((nr, nc))
        
    for r, c in melt_list:
        a[r][c] = 0
    
    return len(melt_list)

t = 0
last_ice = 0

while True:
    melted_ice = bfs()
    if melted_ice == 0:
        break
    
    last_ice = melted_ice

    t += 1

print(t, last_ice)