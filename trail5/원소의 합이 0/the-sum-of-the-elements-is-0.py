from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

for i in range(n):
    for j in range(n):
        t_sum = A[i] + B[j]
        count[t_sum] += 1

for i in range(n):
    for j in range(n):
        diff = - C[i] - D[j]
        if diff in count:
            ans += count[diff]

print(ans)