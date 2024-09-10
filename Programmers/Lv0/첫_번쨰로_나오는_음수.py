def solution(num_list):
    answer = 0
    for i, n in enumerate(num_list):
        if n < 0:
            return i
    return -1