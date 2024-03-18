def count_infected_computers(num_computers, connections):
    graph = {i: set() for i in range(1, num_computers + 1)}

    for computer_a, computer_b in connections:
        graph[computer_a].add(computer_b)
        graph[computer_b].add(computer_a)

    infected_computers = set()
    stack = [1]

    while stack:
        current_computer = stack.pop()

        if current_computer not in infected_computers:
            infected_computers.add(current_computer)
            stack.extend(graph[current_computer] - infected_computers)

    return len(infected_computers) - 1

computers_num = int(input())
computers_connections = int(input())

connections = [tuple(map(int, input().split())) for _ in range(computers_connections)]

result = count_infected_computers(computers_num, connections)
print(result)
