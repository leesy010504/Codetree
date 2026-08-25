from collections import defaultdict

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

map = defaultdict(lambda: float('inf'))

for x, y in points:
    if map[x] >= y:
        map[x] = y

print(sum(map.values()))