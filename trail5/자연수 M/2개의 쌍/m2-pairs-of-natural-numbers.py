N = int(input())
x, y = zip(*[tuple(map(int, input().split())) for _ in range(N)])
x, y = list(x), list(y)

order = sorted(range(N), key=lambda i: y[i])
cnt = [x[i] for i in order]
val = [y[i] for i in order]

l, r = 0, N - 1
ans = 0
while l <= r:
    if l == r:
        if cnt[l] > 0:
            ans = max(ans, val[l] * 2)
        break
    ans = max(ans, val[l] + val[r])
    m = min(cnt[l], cnt[r])
    cnt[l] -= m
    cnt[r] -= m
    if cnt[l] == 0:
        l += 1
    if cnt[r] == 0:
        r -= 1

print(ans)