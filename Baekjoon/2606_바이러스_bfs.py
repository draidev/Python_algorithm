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

    for computer_a, computer_b in connections:
        graph[computer_a].add(computer_b)
        graph[computer_b] .add(computer_a)

    infected_computers = [False] * (num_computers + 1)

    bfs(1, graph, infected_computers)

    return sum(infected_computers) - 1


computers_num = int(input())
computers_connections = int(input())

connections = [tuple(map(int, input().split())) for _ in range(computers_connections)]

result = count_infected_computers(computers_num, connections)
print(result)
