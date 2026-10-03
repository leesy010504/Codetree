n = int(input())
a = [0] + list(map(int, input().split()))
max_val = -float("inf")

t_ans = 0;

for i in range(1, n + 1):
    if t_ans < 0:
        t_ans = a[i]
        
    else:
        t_ans += a[i]
    
    max_val = max(max_val, t_ans)

print(max_val)