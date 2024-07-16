from collections import Counter

# 1
def solution(s):
    c = Counter(s.lower())
    return c['p'] == c['y']

# 2
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
