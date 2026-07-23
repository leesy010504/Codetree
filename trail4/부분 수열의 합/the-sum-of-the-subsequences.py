n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (m + 1)
dp[0] = True

for x in a:
    if x > m:
        continue
    for s in range(m, x - 1, -1):
        if dp[s - x]:
            dp[s] = True

print("Yes" if dp[m] else "No")