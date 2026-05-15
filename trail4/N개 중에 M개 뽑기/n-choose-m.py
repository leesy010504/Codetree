N, M = map(int, input().split())

arr = []

def choose(start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start, N + 1):
        arr.append(i)
        choose(i + 1)
        arr.pop()

choose(1)