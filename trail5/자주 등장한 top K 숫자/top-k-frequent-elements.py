from collections import Counter
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = Counter(arr)

items = sorted(count.items(), key = lambda x:(-x[1], -x[0]))

print(*(num for num, _ in items[:k]))