def solution(cap, n, deliveries, pickups):
    answer = 0
    
    p = deliveries
    q = pickups
    
    cnt = cap
    while p or q:
        for i in (p,q):
            while i and not i[-1]: i.pop()
            
        answer += 2*max(len(p),len(q))
        
        for i in (p,q):
            cnt = cap
            while i and cnt:
                if i[-1] > cnt: 
                    i[-1] -= cnt
                    cnt = 0
                    
                else:
                    cnt -= i[-1]
                    i.pop()
    
    return answer