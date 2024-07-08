def solution(my_string, is_prefix):
    pre_len = len(is_prefix)
    if is_prefix == my_string[:pre_len]:
        return 1
    else:
        return 0