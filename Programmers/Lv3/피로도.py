from collections import deque

def solution(k, dungeons):
    answer = -1
    queue = deque([(k, [])])
    
    while queue:
        k, route = queue.popleft()
        for i in range(len(dungeons)):
            a,b = dungeons[i]
            if (k >= a) and (i not in route):
                temp = route + [i]
                queue.append((k-b,temp))
            else:
                answer = max(answer, len(route))
        # print(queue)
    return answer
