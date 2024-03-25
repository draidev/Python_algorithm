from collections import deque

def bfs(grid, ripe_tomatoes):
    days = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]  # Including current position
    queue = deque(ripe_tomatoes)
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    queue.append((nx, ny))
        if queue:
            days += 1
    
    for row in grid:
        if 0 in row:
            return -1
    return days

def min_days_to_ripen(M, N, H, boxes):
    ripe_tomatoes = []
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[h][i][j] == 1:
                    ripe_tomatoes.append((i, j))
    min_days = bfs(boxes[0], ripe_tomatoes)
    return min_days

# Read input
M, N, H = map(int, input().split())
boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        row = list(map(int, input().split()))
        box.append(row)
    boxes.append(box)

# Calculate and print the result
result = min_days_to_ripen(M, N, H, boxes)
print(result)