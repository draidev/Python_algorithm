def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]

    mok, nam = divmod(s,n)
    mok_list = [mok]*n
    if nam==0:
        return mok_list
    else:
        for n in range(nam):
            mok_list[len(mok_list)-n-1] += 1
        return mok_list
