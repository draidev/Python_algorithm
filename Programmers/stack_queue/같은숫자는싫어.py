from collections import deque

def solution(arr):
    answer = []
    queue = deque()
    queue.append(arr[0])
    for a in arr[1:]:
        q = queue.popleft()
        if q == a:
            queue.append(a)
        else:
            answer.append(q)
            queue.append(a)
            
    answer.append(arr[-1])
                
    return answer