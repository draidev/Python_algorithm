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
    
    # 덜익은 토마토의 개수를 구해야 한다.
    unripe_count = 0
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append((i,j))
            elif tomatoes[i][j] == 0:
                unripe_count += 1
                

    # queue에 들어있는 요소가 여러개라면 요소의 개수만큼 반복문을 돌린다.
    while queue:
        size = len(queue)
        for _ in range(size):
            x,y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # [x][y]배열에서 x는 세로의 길이 N, y는 가로의 길이 M
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