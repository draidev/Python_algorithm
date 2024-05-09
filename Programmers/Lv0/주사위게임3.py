def solution(a, b, c, d):
    answer = 0
    abcd_list = [a,b,c,d]
    same_list = list()
    rest_list = list()
    rest2_list = list()
    p, q, r = 0, 0, 0
        
    for i in abcd_list:
        if same_list==[]:
            same_list.append(i)
        elif i in same_list:
            same_list.append(i)
        elif rest_list==[]:
            rest_list.append(i)
        elif i in rest_list:
            rest_list.append(i)
        elif rest2_list==[]:
            rest2_list.append(i)
        else:
            rest2_list.append(i)
            
    
    if same_list!=[]:
        p = same_list[0]
    if rest_list!=[]:
        q = rest_list[0]
    if rest2_list!=[]:
        r = rest2_list[0]
        
    a_len = len(same_list)
    b_len = len(rest_list)
    c_len = len(rest2_list)
        
    print(p,q,r)
                
    if a==b==c==d:
        answer = 1111*a
        
    if a_len==3:
         answer = (10*p+q)**2
    elif b_len==3:
        answer = (10*q+p)**2
    elif c_len==3:
        answer = (10*r+q)**2
        
    if a_len==2 and b_len==2:
        answer = (p+q) * abs(p-q)
    elif len(same_list)==2 and len(rest_list)==1:
        answer = q*r
    elif len(same_list)==1 and len(rest_list)==2:
        answer = p*r
    elif p!=q!=r:
        answer = min(abcd_list)

    return answer