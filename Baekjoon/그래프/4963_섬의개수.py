from collections import deque

def count_island(w, h, imap):
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()

    count = 0
    for x in range(h):
        for y in range(w):
            if imap[x][y] == 1 and visited[x][y] == False:
                # print("imap:", x, y)
                visited[x][y] = True
                queue.append((x,y))

                while queue:
                    qx, qy = queue.popleft()
                    for dx, dy in directions:
                        nx = qx + dx
                        ny = qy + dy
                        if 0<=nx<h and 0<=ny<w and imap[nx][ny] == 1 and visited[nx][ny] == False:
                            # print("nx,ny",nx,ny)
                            visited[nx][ny] = True
                            queue.append((nx,ny))

                count += 1

    return count

w, h = map(int, input().split())

result_list = []
while((w,h) != (0,0)):
    island_map = [list(map(int, input().split())) for _ in range(h)]

    result_list.append(count_island(w, h, island_map))

    w, h = map(int, input().split())
    
for result in result_list:
    print(result)