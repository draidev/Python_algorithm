from collections import deque
import sys
import copy
input = sys.stdin.readline

def make_wall(count):
    if count == 3:
        bfs()
        return

    for x in range(N):
        for y in range(M):
            if lab_map[x][y] == 0:
                lab_map[x][y] = 1
                cnt = make_wall(count+1)
                lab_map[x][y] = 0
            

def bfs(N, M, lab_map):
    queue = deque()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    for x in range(N):
        for y in range(M):
            if lab_map[x][y] == 2:
                queue.append((x,y))

    while queue:
        x, y = queue.popleft()
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

    return count


M, N = map(int, input().split())

lab_map = [list(map(int, input().split())) for _ in range(N)]

result = 0
result = make_wall(0)

print(result)