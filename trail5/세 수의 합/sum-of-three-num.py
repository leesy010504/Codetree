from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
   
count = {}
for x in arr:
    count[x] = count.get(x, 0) + 1

for i in range(n):
    count[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]
        if diff in count and count[diff] > 0:
            answer += count[diff]
            
print(answer)