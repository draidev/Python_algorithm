str = input()

answer = []
str_list = list(str)

for s in str_list:
    if s.isupper():
        answer.append(s.lower())
    else:
        answer.append(s.upper())
        
answer = ''.join(answer)
print(answer)