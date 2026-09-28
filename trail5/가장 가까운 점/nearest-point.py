import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

heap = [(x + y, x, y) for x, y in points]
heapq.heapify(heap)

for _ in range(m):
    d, x, y = heapq.heappop(heap)
    x += 2
    y += 2
    heapq.heappush(heap, (x + y, x, y))

d, x, y = heap[0]
print(x, y)