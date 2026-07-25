from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
answer = 0

for x in arr:
    answer += count[k - x]
    count[x] += 1

print(answer)