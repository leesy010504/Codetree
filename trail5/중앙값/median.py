import heapq

class PriorityQueue:
    def __init__(self, max_heap=False):
        self.items = []
        self.max_heap = max_heap

    def push(self, item):
        heapq.heappush(self.items, -item if self.max_heap else item)

    def pop(self):
        v = heapq.heappop(self.items)
        return -v if self.max_heap else v

    def top(self):
        v = self.items[0]
        return -v if self.max_heap else v

    def size(self):
        return len(self.items)


class MedianFinder:
    def __init__(self):
        self.low = PriorityQueue(max_heap=True)   # 작은 절반, 최댓값이 top
        self.high = PriorityQueue()               # 큰 절반, 최솟값이 top

    def add(self, x):
        if self.low.size() and x > self.low.top():
            self.high.push(x)
        else:
            self.low.push(x)

        if self.low.size() > self.high.size() + 1:
            self.high.push(self.low.pop())
        elif self.high.size() > self.low.size():
            self.low.push(self.high.pop())

    def getMiddle(self):
        return self.low.top()


t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    mf = MedianFinder()
    meds = []

    for i in range(m):
        mf.add(arr[i])
        if (i + 1) % 2 == 1:
            meds.append(mf.getMiddle())

    print(' '.join(map(str, meds)))