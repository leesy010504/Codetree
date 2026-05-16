n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited_cols = [False] * n
selected_values = []
max_of_min = 0


def choice(row):
    global max_of_min

    if row == n:
        c_min = min(selected_values)
        if c_min > max_of_min:
            max_of_min = c_min
        return

    for col in range(n):
        if not visited_cols[col]:
            visited_cols[col] = True
            selected_values.append(grid[row][col])

            choice(row + 1)

            selected_values.pop()
            visited_cols[col] = False

choice(0)

print(max_of_min)