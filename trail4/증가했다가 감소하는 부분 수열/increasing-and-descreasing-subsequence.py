n = int(input())
seq = list(map(int, input().split()))

inc_dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if seq[i] > seq[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

dec_dp = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if seq[i] > seq[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, inc_dp[i] + dec_dp[i] - 1)

print(ans)