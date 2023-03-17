def solution(queue1, queue2):
    answer = int(1e9)

    n1 = len(queue1)
    
    s_ = 0
    e_ = n1-1
    
    d = queue1 + queue2
    n = len(d)
    
    target = sum(d)
    if target&1: return -1
    target //= 2
    
    e = 0
    tmp = d[0]
    for s in range(n):
        while tmp < target and e - s < n:
            e += 1
            tmp += d[e%n]
            
        if tmp == target:
            res = s-s_
            if e-e_ < 0:
                res += e_ - e + n
            else:
                res += e - e_
            answer = min(answer, res)
                
        tmp -= d[s%n]
    
    answer = answer if answer != int(1e9) else -1
    
    return answer