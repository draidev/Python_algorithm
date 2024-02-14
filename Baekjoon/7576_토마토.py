from collections import deque

def main():
    M, N = map(int,input().split())
    
    box = [list(map(int, input().split())) for _ in range(N)]
    result = count_tomato(box, M, N)
    print(result)
    
def count_tomato(tomatoes, M, N):
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    queue = deque()
    days = 0
    
    unripe_count = 0
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append((i,j))
            elif tomatoes[i][j] == 0:
                unripe_count += 1
                
    while queue:
        size = len(queue)
        for _ in range(size):
            x,y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx and nx < N and 0 <= ny and ny < M and tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = 1
                    unripe_count -= 1
                    queue.append((nx, ny))
                    
        days += 1
        
    if unripe_count == 0:
        return days - 1
    else:
        return -1
                    

    
if __name__=='__main__':
    main()