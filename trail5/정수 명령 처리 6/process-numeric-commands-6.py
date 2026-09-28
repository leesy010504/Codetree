import heapq

N = int(input())
commands = []

class PriorityQueue():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def pop(self):
        if self.empty():
            raise Exception("Priority Queue is empty")
        return -heapq.heappop(self.items)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            raise Exception("Priority Queue is empty")
        return -self.items[0]

pq = PriorityQueue()

for _ in range(N):
    line = input().split()
    command = line[0]

    if command == "push":
        pq.push(int(line[1]))
    elif command == "pop":
        print(pq.pop())
    elif command == "size":
        print(pq.size())
    elif command == "empty":
        print(int(pq.empty()))
    elif command == "top":
        print(pq.top())