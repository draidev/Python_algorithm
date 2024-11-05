from collections import deque

# DFS 함수 정의 (스택 사용)
def dfs_stack(graph, v):
    visited = [False] * (n + 1)
    stack = [v]
    result = []

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            result.append(node)

            # 인접 노드를 작은 번호 순으로 방문하기 위해 역순으로 스택에 추가
            for neighbor in sorted(graph[node], reverse=True):
                if not visited[neighbor]:
                    stack.append(neighbor)

    return result

# BFS 함수 정의
def bfs(graph, v):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                
    return result

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행 (스택 사용)
dfs_result = dfs_stack(graph, v)
print(' '.join(map(str, dfs_result)))

# BFS 실행
bfs_result = bfs(graph, v)
print(' '.join(map(str, bfs_result)))
