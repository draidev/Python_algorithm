from collections import defaultdict
import sys
input = sys.stdin.readline

def find_parents(n, edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parents = [0] * (n+1)
    visited = [False] * (n+1)
    stack = [1]

    while stack:
        node = stack.pop()
        visited[node] = True

        for child in graph[node]:
            if not visited[child]:
                parents[child] = node
                stack.append(child)

    for i in range(2, n+1): 
        print(parents[i])

N = int(input())

edges = [list(map(int,input().split())) for _ in range(N - 1)]

find_parents(N, edges)