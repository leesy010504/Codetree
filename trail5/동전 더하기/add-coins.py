n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
answer = 0

for i in range(n - 1, -1, -1):
    while k >= coins[i]:
        k -= coins[i]
        answer += 1

print(answer)