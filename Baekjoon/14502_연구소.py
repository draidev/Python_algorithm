from collections import deque

M, N = map(int, input().split())

lab_map = [list(map(int, input().split())) for _ in range(N)]

make_wall(N, M, lab_map)

def make_wall(count, N, M, lab_map):
    if count == 3:
        bfs(N, M, lab_map)
        return

    for x in range(N):
        for y in range(M):
            if lab_map[x][y] == 0:
                lab_map[x][y] = 1
                make_wall(count+1, x, y, lab_map)
                lab_map[x][y] = 0

def bfs(N, M, lab_map):
    queue = deque()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    for x in range(N):
        for y in range(M):
            if lab_map[x][y] == 2:
                queue.append((x,y))

    while queue:
        x, y = queue.leftpop()
        for dx, dy in directions:
            nx = dx + x
            ny = dy + y
            if 0<=nx<N and 0<=ny<M and lab_map[nx][ny] == 0:
                lab_map[nx][ny] = 2
                queue.append((nx,ny))
    
    count = 0
    for x in range(N):
        for y in range(M):
            if lab_map[x][y] == 0:
                count += 1