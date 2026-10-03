N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

items = []

for i in range(N):
    items.append((w[i], v[i]))

def ratio(item):
    weight, value = item
    return value / weight

items.sort(key=ratio, reverse=True)

ans = 0
for wi, vi in items:
    if M >= wi:
        M -= wi
        ans += vi
    else:
        ans += vi * M / wi
        break

print(f"{ans:.3f}")