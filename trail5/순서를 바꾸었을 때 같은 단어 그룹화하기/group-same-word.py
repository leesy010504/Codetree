from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]
groups = defaultdict(int)

for i in range(n):
    key = ''.join(sorted(words[i]))
    groups[key] += 1

print(max(groups.values()))