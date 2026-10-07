N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]

arr = [0] * (N + 1)
for x in missing:
    arr[x] = 1

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i]

ans = B
for i in range(K, N + 1):
    ans = min(ans, prefix[i] - prefix[i - K])

print(ans)