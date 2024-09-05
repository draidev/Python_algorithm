def solution(n, slicer, num_list):
    answer = []
    s_a = slicer[0]
    s_b = slicer[1]
    s_c = slicer[2]
    
    if n==1:
        answer = num_list[:s_b+1]
    if n==2:
        answer = num_list[s_a:]
    if n==3:
        answer = num_list[s_a:s_b+1]
    if n==4:
        answer = num_list[s_a:s_b+1:s_c]

    return answer