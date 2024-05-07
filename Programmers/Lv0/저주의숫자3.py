def div_3(num):
    if num%3==0:
        num += 1
    
    return num

def contain_3(num):
    str_list = list(str(num))
    
    for s in str_list:
        if s=='3':
            num += 1
            return contain_3(num)
    
    print("#1", num)
    num = div_3(num)
        
    return num
        

def solution(n):
    answer = 0
    for _ in range(n):
        answer = div_3(answer)
        answer = contain_3(answer)
        answer += 1
        
    return answer - 1