def min_spaces_to_pass(N, M, maze):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M and maze[x][y] == '1'

    queue = [(0,0,1)]
    visited = set()

    i = 0
    while queue:
        x, y, steps = queue.pop(0)
    	
        if (x, y) == (N-1, M-1):
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,steps+1))

    return -1

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

result = min_spaces_to_pass(N, M, maze)
if result != -1:
    print(result)
else:
    print('fail')
