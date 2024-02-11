import sys
sys.setrecursionlimit(10**6)

def dfs(adj_matrix, visited, x, y, M, N):
    if x < 0 or x >= M or y < 0 or y >= N or visited[x][y] or adj_matrix[x][y] == 0:
        return
    
    visited[x][y] = True
    dfs(adj_matrix, visited, x - 1, y, M, N)
    dfs(adj_matrix, visited, x + 1, y, M, N)
    dfs(adj_matrix, visited, x, y - 1, M, N)
    dfs(adj_matrix, visited, x, y + 1, M, N)

def count_cabbage_worms(adj_matrix, M, N):
    visited = [[False for _ in range(N)] for _ in range(M)]
    worms_count = 0

    for i in range(M):
        for j in range(N):
            if not visited[i][j] and adj_matrix[i][j] == 1:
                dfs(adj_matrix, visited, i, j, M ,N)
                worms_count += 1

    return worms_count

def main():
    T = int(input())

    result = list()
    for _ in range(T):
        M, N, K = map(int, input().split())
        adj_matrix = [[0 for _ in range(N)] for _ in range(M)]
        
        for _ in range(K):
            X, Y = map(int, input().split())
            adj_matrix[X][Y] = 1

        worms_required = count_cabbage_worms(adj_matrix, M, N)
        result.append(worms_required)

    for r in result:
        print(r)

if __name__=='__main__':
    main()