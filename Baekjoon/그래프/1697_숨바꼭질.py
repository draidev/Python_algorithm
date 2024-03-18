from collections import deque

def find_fastest_time(N, K):
    visited = set()
    queue = deque([(N, 0)])

    while queue:
        position, time = queue.popleft()
        if position == K:
            return time

        if position not in visited:
            visited.add(position)

            if position * 2 <= 100000:
                queue.append((position * 2, time + 1))

            if position - 1 >= 0:
                queue.append((position - 1, time + 1))
            if position + 1 <= 100000:
                queue.append((position + 1, time +1))

N, K = map(int, input().split())

print(find_fastest_time(N, K))