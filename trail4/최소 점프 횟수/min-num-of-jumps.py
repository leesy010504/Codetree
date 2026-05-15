n = int(input())
num = list(map(int, input().split()))
min_cnt = float('inf')

def jump(idx, count):
    global min_cnt

    if count >= min_cnt:
        return
    
    if idx >= n - 1:
        min_cnt = min(min_cnt, count)
        return
    
    for dist in range(1, num[idx] + 1):
        jump(idx + dist, count + 1)

jump(0,0)

print(min_cnt if min_cnt != float('inf') else -1)