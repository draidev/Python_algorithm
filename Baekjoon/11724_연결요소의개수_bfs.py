import sys
from collections import deque

def count_connected(edges, N):
    graph = {i:set() for i in range(1, N+1)}

    for u, v in edges:
        graph[u].add(v) 
        graph[v].add(u)

    visited = [False for _ in range(0, N+1)]
    queue = deque()

    connected_count = 0
    for i in range(1, N+1):
        if graph[i] != () and visited[i] == False:
            queue.append(i)
            visited[i] = True
        else: 
            continue

        while queue:
            n = queue.popleft()
            
            for neighbor in graph[n]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    queue.append(neighbor)

        connected_count += 1
    
    return connected_count



N, M = map(int, sys.stdin.readline().split())

edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

result = count_connected(edges, N)
print(result)