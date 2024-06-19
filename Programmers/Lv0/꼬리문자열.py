# update 꼬리문자열.py \\ Lv0 \\ https://school.programmers.co.kr/learn/courses/30/lessons/181841
def solution(str_list, ex):
    answer = ''
    
    for st in str_list:
        if ex not in st:
            answer += st
    
    return answer`
