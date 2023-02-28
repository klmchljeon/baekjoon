def ins(i):
    idx = d[i]-1
    bki = idx//sqn
    s,sbk = finds(idx)
    e,ebk = finde(idx)
    
    val = 0

    if bucket[bki][1] == None:
        bucket[bki][1] = 0

    if sbk!=None:
        tmp = abs(i-lst[s])
        val += -bucket[sbk][3] + tmp
        bucket[sbk][3] = tmp
        bucket[sbk][2] = bki
        bucket[bki][0] = sbk

    elif s!=None:
        tmp = abs(i-lst[s])
        val += tmp
        bucket[bki][1] += tmp

    if ebk!=None:
        tmp = abs(lst[e]-i)
        val += -bucket[bki][3] + tmp
        bucket[bki][3] = tmp
        bucket[ebk][0] = bki
        bucket[bki][2] = ebk

    elif e!=None:
        tmp = abs(lst[e]-i)
        val += tmp
        bucket[bki][1] += tmp

        if sbk==None and s!=None:
            tmp = abs(lst[e]-lst[s])
            val -= tmp
            bucket[bki][1] -= tmp

    return val

def remov(i):
    idx = d[i]-1
    bki = idx//sqn
    s,sbk = finds(idx)
    e,ebk = finde(idx)
    
    val = 0

    if sbk!=None and ebk!=None:
        val -= bucket[sbk][3] + bucket[bki][3]
        bucket[bki] = [None]*3 + [0]
        bucket[sbk][2] = ebk
        bucket[ebk][0] = sbk

        tmp = abs(lst[e]-lst[s])
        val += tmp
        bucket[sbk][3] = tmp

    elif sbk!=None:
        if e!=None:
            tmp = abs(lst[e]-i)
            val -= tmp
            bucket[bki][1] -= tmp

            tmp = abs(lst[e]-lst[s])
            val += -bucket[sbk][3] + tmp
            bucket[sbk][3] = tmp

        else:
            val -= bucket[sbk][3]
            bucket[bki][0] = None
            bucket[bki][1] = None
            bucket[sbk][2] = None
            bucket[sbk][3] = 0

    elif ebk!=None:
        if s!=None:
            tmp = abs(i-lst[s])
            val -= tmp
            bucket[bki][1] -= tmp

            tmp = abs(lst[e]-lst[s])
            val += -bucket[bki][3] + tmp
            bucket[bki][3] = tmp

        else:
            val -= bucket[bki][3]
            bucket[ebk][0] = None
            bucket[bki][1] = None
            bucket[bki][2] = None
            bucket[bki][3] = 0

    else:
        if s!=None:
            tmp = abs(i-lst[s])
            val -= tmp
            bucket[bki][1] -= tmp

        if e!=None:
            tmp = abs(lst[e]-i)
            val -= tmp
            bucket[bki][1] -= tmp

            if s!=None:
                tmp = abs(lst[e]-lst[s])
                val += tmp
                bucket[bki][1] += tmp

    return val

def finde(idx):
    bki = idx//sqn
    e = (bki+1)*sqn
    
    ebk = bucket[bki][2]
    if ebk == None:
        for i in range(bki+1,sqn):
            if bucket[i][1] != None:
                ebk = i
                break

    for i in range(idx+1,e):
        if lst[i] != None:
            return i,None

    if ebk == None:
        return None,None
    
    s = ebk*sqn
    e = (ebk+1)*sqn
    for i in range(s,e):
        if lst[i] != None:
            return i,ebk
        
def finds(idx):
    bki = idx//sqn
    s = bki*sqn
    
    sbk = bucket[bki][0]
    if sbk == None:
        for i in range(bki-1,-1,-1):
            if bucket[i][1] != None:
                sbk = i
                break

    for i in range(idx-1,s-1,-1):
        if lst[i] != None:
            return i,None
        
    if sbk == None:
        return None,None
    
    s = sbk*sqn
    e = (sbk+1)*sqn
    for i in range(e-1,s-1,-1):
        if lst[i] != None:
            return i,sbk

n,k = map(int,input().split())
d = tuple(map(int,input().split()))

sqn = int(n**0.5)+1
bucket = [[None]*3+[0] for _ in range(sqn+1)]
lst = [None]*(sqn**2)

res = 0
for i in range(k):
    res += ins(i)
    lst[d[i]-1] = i

ans = res
for i in range(k,n):
    res += ins(i)
    lst[d[i]-1] = i

    res += remov(i-k)
    lst[d[i-k]-1] = None

    ans = min(ans,res)

print(ans)