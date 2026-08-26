from sortedcontainers import SortedDict

n = int(input())
arr = [input().strip() for _ in range(n)]

sd = SortedDict()

for i in range(n):
    sd[arr[i]] = sd.get(arr[i], 0) + 1

for k, v in sd.items():
    print(k, v)