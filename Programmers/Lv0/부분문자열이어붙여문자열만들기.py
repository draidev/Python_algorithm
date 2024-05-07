def solution(my_strings, parts):
    answer = ''
    
    temp_list = list()
    for s, p in zip(my_strings, parts):        
        temp_list.append(s[p[0]:p[1]+1])
        
    answer = ''.join(temp_list)
    
    return answer