from collections import deque
import itertools

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

''' 조합(combination) 사용 '''
# number_comb = list(itertools.combinations(numbers, 3))

# answer = 0
# for i in number_comb:
#     if sum(i) <= M:
#         answer = max(answer, sum(i))
    
# print(answer)

''' for loop 사용 '''
answer = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            cur_sum = numbers[i] + numbers[j] + numbers[k]
            if cur_sum <= M and cur_sum > answer:
                answer = cur_sum
                
print(answer)