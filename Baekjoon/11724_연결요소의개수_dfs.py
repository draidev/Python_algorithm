import sys
sys.setrecursionlimit(10**6)

def count_connect(N, edges):
    graph = {i:[] for i in range(1, N+1)}
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = {i:False for i in range(1, N+1)}
    
    connected_components = 0
    for node in range(1, N+1):
        if not visited[node]:
            dfs(graph, node, visited)
            connected_components += 1
            
    return connected_components

def dfs(graph, node, visited):
    stack = list()
    
    stack.append(node)
    visited[node] = True
    
    
    while stack:    
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
        

N, M = map(int, sys.stdin.readline().split())

edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
result = count_connect(N, edges)
print(result)