def solution(my_string, m, c):
    answer = ''
    i = 0
    temp_str = ''
    temp_list = list()

    for st in my_string:
        temp_str += st
        if i == m-1:
            temp_list.append(temp_str)
            temp_str = ''
            i=0
        else:
            i+=1
        
    for t in temp_list:
        answer += t[c-1]