from sortedcontainers import SortedDict

n = int(input())

sd = SortedDict()

for _ in range(n):
    w = input().rstrip()
    sd[w] = sd.get(w, 0) + 1

for k, v in sd.items():
    print(f"{k} {v / n * 100:.4f}")