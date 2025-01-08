def check(level,diffs,times,limit):
    n = len(diffs)
    t = 0
    prev = 0
    for i in range(n):
        cur = times[i]
        
        if diffs[i] > level:
            cur += (diffs[i]-level)*(times[i] + prev)
            
        t += cur
        prev = times[i]
        
    return t <= limit

def solution(diffs, times, limit):
    s,e = 0,max(diffs)
    while s+1<e:
        mid = (s+e)//2
        
        if check(mid,diffs,times,limit):
            e = mid
            
        else:
            s = mid
    
    return e