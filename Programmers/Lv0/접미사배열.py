def solution(my_string):
    answer = []
    for st in range(len(my_string)):
        print(st ,my_string[st:])
        answer.append(my_string[st:])
        
    return sorted(answer)