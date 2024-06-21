# update 주사위게임1.py \\ Lv0 \\https://school.programmers.co.kr/learn/courses/30/lessons/181839

def solution(a, b):
    answer = 0
    if a%2==1 and b%2==1:
        answer = a**2 + b**2
    elif (a+b)%2==1:
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
        
    return answer
