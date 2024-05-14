import heapq

def solution(operations):
    answer = []
    oper_list = list()
    num_list = list()
    
    for operation in operations:
        a,b = operation.split(' ')
        oper_list.append((a,b))
        
        if a=='I':
            heapq.heapify(num_list)
            heapq.heappush(num_list, int(b))
        
        if num_list!=[]:
            if a=='D':
                if b=='1':
                    num_list = [-1*x for x in num_list]
                    heapq.heapify(num_list)
                    heapq.heappop(num_list)
                    num_list = [-1*x for x in num_list]
                if b=='-1':
                    heapq.heapify(num_list)
                    heapq.heappop(num_list)
                    
        if num_list==[]:
            answer = [0,0]
        else:
            answer = [max(num_list), min(num_list)]
    
    return answer
