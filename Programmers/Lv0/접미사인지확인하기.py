def solution(my_string, is_suffix):
    answer = 0
    
    for m in range(len(my_string)):
        if my_string[m:]==is_suffix:
            answer = 1 
    
    return answer