n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

if t >= 2 * n:
    t %= (2 * n)

for _ in range(t):
    tmp_h = u[n - 1]
    tmp_l = d[n - 1]
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
        d[i] = d[i - 1]
    d[0] = tmp_h
    u[0] = tmp_l

print(*u)
print(*d)