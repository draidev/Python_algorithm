from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))

    queue = deque([(i, priority) for i, priority in enumerate(importance)])
    printed = 0

    while queue:
        cur_imp = queue.popleft()

        ishigher = False
        if any(cur_imp[1] < q[1] for q in queue):
            queue.append(cur_imp)
        else:
            printed += 1
            if cur_imp[0] == M:
                print(printed)
        
        

        
    