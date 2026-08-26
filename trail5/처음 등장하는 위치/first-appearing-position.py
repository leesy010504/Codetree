from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))

sd = SortedDict()

for i in range(n):
    if arr[i] in sd:
        continue
    else:
        sd[arr[i]] = i + 1

for k, v in sd.items():
    print(k, v)