M = int(input())
A, B = map(int, input().split())

min_count = M + 1
max_count = 0

for answer in range(A, B + 1):
    left = 1
    right = M
    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1

        if mid == answer:
            break
        elif mid < answer:
            left = mid + 1
        else:
            right = mid - 1

    min_count = min(min_count, count)
    max_count = max(max_count, count)

print(min_count, max_count)