K, N = map(int, input().split())
ans = []

def find(cnt):
    if cnt == N:
        print(*ans)
        return

    for i in range(1, K + 1):
        ans.append(i)
        find(cnt + 1)
        ans.pop() 

find(0)