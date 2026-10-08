n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

p = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        p[i + 1][j + 1] = a[i][j] + p[i][j + 1] + p[i + 1][j] - p[i][j]

ans = 0
for i in range(k, n + 1):
    for j in range(k, n + 1):
        ans = max(ans, p[i][j] - p[i - k][j] - p[i][j - k] + p[i - k][j - k])

print(ans)