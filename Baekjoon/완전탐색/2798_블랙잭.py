from collections import deque
import itertools

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

number_comb = list(itertools.combinations(numbers, 3))

answer = 0
for i in number_comb:
    if sum(i) <= M:
        answer = max(answer, sum(i))
    
print(answer)