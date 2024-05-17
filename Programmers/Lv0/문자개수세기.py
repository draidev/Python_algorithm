def solution(my_string):
    answer = [0 for _ in range(52)]

    for s in my_string:
        if s.islower():
            s_index = ord(s) - 97 + 26
        else:
            s_index = ord(s) - 65
        
        answer[s_index] += 1
        
    return answer