n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_sum(r, c, w, h):
    dr, dc = [-1, -1, 1, 1], [1, -1, -1, 1]
    ws = [w, h, w, h]
    total = 0

    for i in range(4):
        for _ in range(ws[i]):
            r, c = r + dr[i], c + dc[i]
            if not (0 <= r < n and 0 <= c < n):
                return 0
            total += grid[r][c]
        
    return total 

ans = 0
for r in range(n):
    for c in range(n):
        for w in range(1, n):
            for h in range(1, n):
                ans = max(ans, get_sum(r, c, w, h))

print(ans)