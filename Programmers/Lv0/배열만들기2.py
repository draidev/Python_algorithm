def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        flag = 1
        if i%5==0:
            str_list = list(str(i))
            
            for str_ in str_list:
                if str_ != '5' and  str_ != '0':
                    flag = 0
                    
            if flag == 1:
                join_str = ''.join(str_list)
                answer.append(int(join_str))
                
    if answer == []:
        answer = [-1]
    
    return answer