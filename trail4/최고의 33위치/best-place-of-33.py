n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coins = 0

for row in range(n - 2):
    for col in range(n - 2):
        
        current_coins = 0
        for i in range(3):
            for j in range(3):
                current_coins += grid[row + i][col + j]
        
        max_coins = max(max_coins, current_coins)

print(max_coins)