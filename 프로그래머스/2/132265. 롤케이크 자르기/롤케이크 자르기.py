def solution(topping):
    answer = 0
    llst = [0]*10001
    l = 0
    
    rlst = [0]*10001
    r = 0
    for i in topping:
        rlst[i] += 1
        if rlst[i] == 1:
            r += 1
            
    for i in topping:
        llst[i] += 1
        if llst[i] == 1:
            l += 1
            
        rlst[i] -= 1
        if rlst[i] == 0:
            r -= 1
            
        answer += l==r
    
    return answer