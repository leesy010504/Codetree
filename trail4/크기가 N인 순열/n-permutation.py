n = int(input())
visited = [False] * (n + 1)
ans = []

def choose(num):
    if num == n + 1:
        print(*ans)
        return

    for i in range(1, n + 1):
        if visited[i] == True:
            continue
        
        visited[i] = True
        ans.append(i)
        choose(num + 1)
        ans.pop()
        visited[i] = False

choose(1)
