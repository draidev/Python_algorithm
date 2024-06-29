def solution(arr, idx):
    answer = idx
    for i in arr[idx:]:
        if i==1:
            return answer
        else:
            answer+=1
    
    return -1