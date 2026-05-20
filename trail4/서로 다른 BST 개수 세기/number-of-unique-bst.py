n = int(input())

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    for j in range(1, n + 1):
        left_node = j - 1
        right_node = i - j
        dp[i] += dp[left_node] * dp[right_node]

print(dp[n])