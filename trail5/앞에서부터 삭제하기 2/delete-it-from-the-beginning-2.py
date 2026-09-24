n = int(input())
arr = list(map(int, input().split()))

suffix_sum = [0] * (n + 1)

suffix_min = [0] * n

for i in range(n - 1, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    if i == n - 1:
        suffix_min[i] = arr[i]
    else:
        suffix_min[i] = min(arr[i], suffix_min[i + 1])

answer = float('-inf')

for k in range(1, n - 1):
    total = suffix_sum[k]
    minimum = suffix_min[k]

    count = n - k - 1

    average = (total - minimum) / count

    answer = max(answer, average)

print(f"{answer:.2f}")