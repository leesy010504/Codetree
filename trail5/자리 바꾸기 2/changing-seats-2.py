n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

seat = list(range(n + 1))
visited = [{i} for i in range(n + 1)]

for _ in range(3):
    for a, b in edges:
        p, q = seat[a], seat[b]
        seat[a], seat[b] = q, p
        visited[p].add(b)
        visited[q].add(a)

for i in range(1, n + 1):
    print(len(visited[i]))