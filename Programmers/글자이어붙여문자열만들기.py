def solution(my_string, index_list):
    answer = []
    for i in index_list:
        answer.append(my_string[i])
        
    answer = ''.join(answer)
    
    return answer