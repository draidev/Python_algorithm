def solution(q, r, code):
    answer = ''
    
    v = 0
    for c in range(len(code)):
        if r == (c%q):
            answer += code[c]        
    
    return answer