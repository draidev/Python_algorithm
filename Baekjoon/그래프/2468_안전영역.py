# Baekjoon / https://www.acmicpc.net/problem/2468 / Complete
from collections import deque

def count_safe_place(N, graph, safe_height):
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    count = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y] > safe_height and visited[x][y]==False:
                queue.append((x,y))
                visited[x][y] = True
                count += 1
                
                while queue:
                    nx, ny = queue.popleft()
                    for d in directions:
                        dx = nx + d[0]
                        dy = ny + d[1]
                        if 0<=dx<N and 0<=dy<N and graph[dx][dy]>safe_height and visited[dx][dy]==False:
                            visited[dx][dy] = True
                            queue.append((dx,dy))

    # 만약 물에 잠기는 지역이 하나도 없다면 전체가 안전지역이므로 1을 반환
    if count == 0:
        return 1
                            
    return count            
                    

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

count_list = []

max_num = max([max(x) for x in graph])

for safe_height in range(1,max_num+1):
    count_list.append(count_safe_place(N, graph, safe_height))
    
print(max(count_list))
