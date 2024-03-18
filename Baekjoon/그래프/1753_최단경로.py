import heapq

def dijkstra(graph, start):
    # 시작 정점부터 각 정점까지의 최단 거리를 저장할 리스트
    distances = [float('inf')] * (len(graph) + 1)
    distances[start] = 0

    # 우선순위 큐를 이용하여 방문할 정점을 관리
    queue = [(0, start)]

    while queue:
        # 현재 정점까지의 최단 거리와 정점 번호를 꺼냄
        current_distance, current_vertex = heapq.heappop(queue)

        # 현재 정점의 최단 거리가 이미 구해진 거리보다 크다면 스킵
        if current_distance > distances[current_vertex]:
            continue

        # 현재 정점에서 이동 가능한 정점들을 순회
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # 이동한 거리가 기존에 저장된 거리보다 작다면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances[1:]

# 입력 처리
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘을 이용하여 최단 경로 계산
shortest_paths = dijkstra(graph, K)

# 결과 출력
for distance in shortest_paths:
    if distance == float('inf'):
        print("INF")
    else:
        print(distance)