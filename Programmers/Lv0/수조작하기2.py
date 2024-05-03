def solution(numLog):
    answer = []
    temp = 0
    for i in range(len(numLog)):
        if i == 0:
            temp = numLog[i]
            continue
            
        subnum = numLog[i] - temp
        if subnum == 1:
            answer.append('w')
        elif subnum == -1:
            answer.append('s')
        elif subnum == 10:
            answer.append('d')
        else:
            answer.append('a')
        temp = numLog[i]
    
    answer = ''.join(answer)
    
    return answer