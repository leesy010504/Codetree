from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

r -= 1
c -= 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc):
    visited = [[False] * n for _ in range(n)]
    q = deque()

    q.append((sr, sc))
    visited[sr][sc] = True

    limit = grid[sr][sc]

    candidates = []

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if not (0 <= nr < n and 0 <= nc < n):
                continue

            if visited[nr][nc]:
                continue

            if grid[nr][nc] >= limit:
                continue

            visited[nr][nc] = True
            q.append((nr, nc))
            candidates.append((nr, nc))

    if not candidates:
        return None

    candidates.sort(
        key=lambda pos: (
            -grid[pos[0]][pos[1]],
            pos[0],
            pos[1]
        )
    )

    return candidates[0]


for _ in range(k):
    nxt = bfs(r, c)

    if nxt is None:
        break

    r, c = nxt

print(r + 1, c + 1)
