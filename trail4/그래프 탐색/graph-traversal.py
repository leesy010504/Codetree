n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
count = 0

def dfs(v):
    global count
    visited[v] = True
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += 1
            dfs(neighbor)

dfs(1)

print(count)