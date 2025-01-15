def solution(lst, k):
    n = len(lst)
    tmp = 0
    e = 0
    
    p = []
    for s in range(n):
        while e < n and tmp < k:
            tmp += lst[e]
            e += 1
            
        if tmp == k:
            p.append((s,e-1))
    
        tmp -= lst[s]
        
    res = min(p,key = lambda x:(x[1]-x[0],x[0]))
    
    return res