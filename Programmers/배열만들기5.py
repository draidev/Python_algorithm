def solution(intStrs, k, s, l):
    answer = []
    for int_str in intStrs:
        temp_int = int(int_str[s:s+l])
        if temp_int > k:
            answer.append(temp_int)
        
    return answer
