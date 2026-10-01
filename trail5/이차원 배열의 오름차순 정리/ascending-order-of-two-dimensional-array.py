n = int(input())
k = int(input())

left = 1
right = k

while left <= right:
    mid = (left + right) // 2

    count = 0

    for i in range(1, n + 1):
        count += min(n, mid // i)

    if count >= k:
        right = mid - 1
    else:
        left = mid + 1

print(left)