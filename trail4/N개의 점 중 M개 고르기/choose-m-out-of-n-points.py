n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

def get_dist(idx1, idx2):
    dist = pow(points[idx1][0] - points[idx2][0], 2) + pow(points[idx1][1] - points[idx2][1], 2)
    return dist

min_dist = float('inf')
selected_points = []

def choice(idx):
    global min_dist 
    if len(selected_points) == m:
        current_dist = 0
        for i in range(m):
            for j in range(i + 1, m):
                dist = get_dist(selected_points[i], selected_points[j])
                if dist > current_dist:
                    current_dist = dist
                    
        if current_dist < min_dist:
            min_dist = current_dist
        return
    
    if idx == n:
        return
    selected_points.append(idx)
    choice(idx + 1)
    selected_points.pop()

    choice(idx + 1)

choice(0)
print(min_dist)