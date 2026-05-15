K, N = map(int, input().split())

arr = []

def count(idx):
    if idx == N:
        print(*arr)
        return 0

    for i in range(1, K + 1):
        if len(arr) >= 2 and arr[-1] == i and arr[-2] == i:
            continue
        arr.append(i)
        count(idx + 1)
        arr.pop()

count(0)