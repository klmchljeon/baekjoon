def solution(numlist, n):
    answer = []
    
    for k in range(len(numlist)):
        res = 10000
        for i in range(len(numlist)):
            if res > abs(numlist[i]-n):
                res = abs(numlist[i]-n)
                
        fir = n + res
        if fir in numlist:
            answer.append(fir)
            numlist.remove(fir)
            continue
            
        sec = n - res
        answer.append(sec)
        numlist.remove(sec)
        
    return answer