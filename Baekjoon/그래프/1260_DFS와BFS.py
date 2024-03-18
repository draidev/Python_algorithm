from collections import defaultdict, deque

def input_graph():
    N, M, V = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return N, V, graph

def dfs(N, V, graph):
    visited = set()
    stack = [V]

    while stack:
        current_vertex = stack.pop()
        if current_vertex not in visited:
            print(current_vertex, end=' ')
            visited.add(current_vertex)
            stack.extend(sorted(set(graph[current_vertex]) - visited, reverse=True))

def bfs(N, V, graph):
    visited = set()
    queue = deque([V])

    while queue:
        current_vertex = queue.popleft()
        if current_vertex not in visited:
            print(current_vertex, end=' ')
            visited.add(current_vertex)
            queue.extend(sorted(set(graph[current_vertex]) - visited))

def main():
    N, V, graph = input_graph()

    # DFS
    dfs(N, V, graph)
    print()

    # BFS
    bfs(N, V, graph)

if __name__ == "__main__":
    main()