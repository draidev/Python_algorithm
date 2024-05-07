import heapq

def solution(n, works):
    if sum(works) < n:
        return 0
    else:
        works = [-1*w for w in works]
        heapq.heapify(works)
        
        for _ in range(n):
            work = heapq.heappop(works)
            heapq.heappush(works, work+1)
    
    answer = sum([w**2 for w in works])
    
    return answer