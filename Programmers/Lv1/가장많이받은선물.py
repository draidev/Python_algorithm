def solution(friends, gifts):
    answer = 0
    friends_dict = {}
    gift_index = {}
    next_month = {}
    
    for f in friends:
        friends_dict[f] = {}
        next_month[f] = {}
        gift_index[f] = [0, 0, 0]
        for t in friends:
            friends_dict[f][t] = 0
            next_month[f] = 0
    
    for g in gifts:
        giver, taker = g.split(' ')
        friends_dict[giver][taker] += 1
        gift_index[giver][0] += 1
        gift_index[taker][1] += 1
    
    for g in list(gift_index.keys()):
        gift_index[g][2] = gift_index[g][0] - gift_index[g][1]
    
    print(friends_dict)
    print(gift_index)
    
    for f in friends:
        for s in list(friends_dict[f].keys()):
            if f == s:
                continue
                
            if friends_dict[f][s] > friends_dict[s][f]:
                next_month[f] += 1
            
            if (friends_dict[f][s] == 0 and friends_dict[s][f] == 0) or (friends_dict[f][s] == friends_dict[s][f]):
                if (gift_index[f][2] == gift_index[s][2]):
                    continue
                if (gift_index[f][2] > gift_index[s][2]):
                    next_month[f] += 1
            
    answer = max(list(next_month.values()))
    
    return answer
