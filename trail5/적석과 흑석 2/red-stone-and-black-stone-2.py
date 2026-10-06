import heapq

C, N = map(int, input().split())
T = sorted(int(input()) for _ in range(C))
black = sorted(tuple(map(int, input().split())) for _ in range(N))

heap = []
idx = 0
answer = 0
for t in T:
    while idx < N and black[idx][0] <= t:
        heapq.heappush(heap, black[idx][1])
        idx += 1
    while heap and heap[0] < t:
        heapq.heappop(heap)
    if heap:
        heapq.heappop(heap)
        answer += 1
print(answer)