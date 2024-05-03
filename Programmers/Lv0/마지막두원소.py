def solution(num_list):
    answer = []
    
    last_num = num_list[-1]
    pre_num = num_list[-2]
    
    if last_num > pre_num:
        answer = last_num - pre_num
    else:
        answer = 2*last_num
    
    num_list.append(answer)
    answer = num_list
    return answer