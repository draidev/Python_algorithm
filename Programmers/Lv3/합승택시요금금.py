# 합승택시요금 Lv3 다익스트라 알고리즘/ https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq

def dijkstra(graph, s):
    priority_queue = [(0, s)]
    distances = {node:float('inf') for node in graph}
    distances[s] = 0
    previous_node = {node:None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_node[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
            
    return previous_node, distances

def solution(n, s, a, b, fares):
    answer = 0
    
    graph = {}
    for start, end, weight in fares:
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        graph[start][end] = weight
        graph[end][start] = weight
        
    # print(graph)
    s_p, s_d = dijkstra(graph, s)
    print(s_p)
    
    cost_list = []
    for s_node, s_dist  in s_d.items():
        _, distances = dijkstra(graph, s_node)
        cost_list.append(s_dist+distances[a]+distances[b])

    answer = min(cost_list)
    
    return answer
