from collections import deque
import sys

N = int(input())

if N == 1:
    print(0)
    sys.exit()

q = deque([(N, 0)])
visited = set([N])

def op1(n):
    return n - 1

def op2(n):
    return n + 1

def op3(n):
    return n // 2 if n % 2 == 0 else n

def op4(n):
    return n // 3 if n % 3 == 0 else n

operation = [op1, op2, op3, op4]

while q:
    curr, cnt = q.popleft()

    for op in operation:
        nxt = op(curr)

        if nxt == 1:
            print(cnt + 1)
            sys.exit()

        if nxt not in visited:
            q.append((nxt, cnt + 1))
            visited.add(nxt)

