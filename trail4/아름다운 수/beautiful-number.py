n = int(input())

count = 0

def solve(current_length):
    global count
    
    if current_length == n:
        count += 1
        return
    
    for i in range(1, 5):
        if current_length + i <= n:
            solve(current_length + i)

solve(0)

print(count)