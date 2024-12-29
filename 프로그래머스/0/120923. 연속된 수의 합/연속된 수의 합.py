def solution(num, total):
    res = []
    if num%2 == 0:
        l = total//(num//2)//2
        r = l+1
        for i in range(num//2):
            res.append(l)
            res.append(r)
            l -= 1
            r += 1
            
        res.sort()
        
    else:
        m = total//num
        res.append(m)
        l = m-1
        r = m+1
        for i in range((num-1)//2):
            res.append(l)
            res.append(r)
            l -= 1
            r += 1
        
        res.sort()
        
    print(res)
    return res