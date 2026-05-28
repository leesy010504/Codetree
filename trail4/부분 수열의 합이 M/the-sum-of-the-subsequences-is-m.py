n, m = map(int, input().split())
A = list(map(int, input().split()))

INF = 10000
dp = [INF] * (m + 1)
dp[0] = 0
for elem in A:
    for i in range(m, elem - 1, -1):
        if not dp[i - elem] == INF:
            dp[i] = min(dp[i], dp[i - elem] + 1)

print(dp[m] if not dp[m] == INF else -1)