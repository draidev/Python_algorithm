def selection_sort(citations):
    for i in range(len(citations)):
        max_idx = i 
        for j in range(i+1, len(citations)):
            if citations[max_idx] < citations[j]:
                max_idx = j
        citations[i], citations[max_idx] = citations[max_idx], citations[i]
        #print(i, citations)
                   
    return citations

def solution(citations):
    citations = selection_sort(citations)
    n = len(citations)
    h = 0
    
    for i in range(n):
        if citations[i] >= i+1:
            h = i+1
        else:
            break
    
    return h