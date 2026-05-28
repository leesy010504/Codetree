n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [10000] * (m + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        if dp[i - coin] != 10000:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[m] == 10000:
    print(-1)
else:
    print(dp[m])