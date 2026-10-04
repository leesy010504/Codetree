n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key = lambda x: (x[1], x[0]))

cnt = 0
end = 0

for s, e in meetings:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
