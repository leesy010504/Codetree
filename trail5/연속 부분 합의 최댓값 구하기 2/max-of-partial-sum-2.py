import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))

ans = INT_MIN

sum_of_nums = 0;

for i in range(1, n + 1):
    if sum_of_nums < 0:
        sum_of_nums = arr[i]
    
    else:
        sum_of_nums += arr[i]
    
    ans = max(ans, sum_of_nums)

print(ans)
