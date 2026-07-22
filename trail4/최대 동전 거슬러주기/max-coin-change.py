N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [-1] * (M + 1)
dp[0] = 0

for i in range(1, M + 1):
    for c in coin:
        if i >= c and dp[i - c] != -1:
            dp[i] = max(dp[i], dp[i - c] + 1)

print(dp[M])