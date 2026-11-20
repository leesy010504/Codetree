n = int(input())
num = list(map(int, input().split()))
total = sum(num)
min_diff = float("inf")
arr = []

def solve(start):
    global min_diff
    if len(arr) == n:
        min_diff = min(min_diff, abs(total - sum(arr) - sum(arr)))
        return
    if start == 2 * n:
        return
    
    arr.append(num[start])
    solve(start + 1)
    arr.pop()

    solve(start + 1)

solve(0)
print(min_diff)