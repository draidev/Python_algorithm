import heapq

def dijkstra(graph, start):
    # 우선 순위 큐에 (거리, 노드) 저장
    priority_queue = [(0, start)]
    # 각 노드까지의 최단 거리를 저장할 딕셔너리
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # 각 노드까지의 최단 경로를 저장할 딕셔너리
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 만약 추출된 노드의 거리가 기록된 최단 거리보다 크면 건너뜁니다
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 이웃 노드로 가는 더 짧은 경로를 찾으면
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def construct_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    return path

# 예제 그래프를 인접 리스트로 표현
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 출발 노드 'A'에서 최단 경로를 찾습니다
distances, previous_nodes = dijkstra(graph, 'A')

# 각 노드까지의 최단 경로를 출력
for node in graph:
    path = construct_path(previous_nodes, 'A', node)
    print(f"Shortest path from A to {node}: {path}, Distance: {distances[node]}")
