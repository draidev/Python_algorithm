from collections import deque

def bfs(start, graph, infected_computers):
    queue = deque([start])
    infected_computers[start] = True

    while queue:
        current_computer = queue.popleft()

        for neighbor in graph[current_computer]:
            if not infected_computers[neighbor]:
                infected_computers[neighbor] = True
                queue.append(neighbor)


def count_infected_computers(num_computers, connections):
    graph = {i:set() for i in range(1, num_computers+1)}

    for pair in connections:
        computer_a, computer_b = pair
        graph[computer_a] = computer_b
        graph[computer_b] = computer_a

    infected_computers = [False] * (num_computer + 1)

    bfs(1, graph, infected_computers)

    return sum(infected_computers) - 1



computers_num = int(input())
computers_connections = input(input())

connections = [tuple(map(int, input())) for _ in computers_connections]

result = count_infected_computers(num_computers, connections)
print(result)
