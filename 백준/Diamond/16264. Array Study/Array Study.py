#Array Study
import sys
from collections import deque
input = sys.stdin.readline

def cal():
    idx = None
    for i in range(sqn,-1,-1):
        if bucket[i]:
            idx = i
            break

    if idx == None: 
        return 0
    
    s = idx*sqn
    e = min((idx+1)*sqn,n)
    for i in range(e-1,s-1,-1):
        if lst[i]:
            return i

t = int(input())
for case in range(t):
    n = int(input())
    n += 1
    arr = tuple(map(int,input().split()))

    prefix = [0,0]
    s = 0
    for i in arr:
        s += i
        prefix.append(s)

    dic = {0:0}
    d = [0]*(n+1)
    for i in range(2,n+1):
        if not prefix[i] in dic:
            dic[prefix[i]] = i

        d[i] = dic[prefix[i]]

    k = max(d)

    sqn = int(n**0.5) + 1

    m = int(input())
    query = []
    for i in range(m):
        a,b = map(int,input().split())
        query.append((a,b+1))

    f = lambda x:(x[0]//sqn,x[1])
    query.sort(key = f)

    deq = [deque([]) for _ in range(k+1)]

    lst = [0]*(n+1)
    bucket = [0]*(sqn+1)
    res = 0

    pa,pb = query[0]
    for i in range(pa,pb+1):
        if deq[d[i]]:
            tmp = deq[d[i]][-1] - deq[d[i]][0]
            lst[tmp] -= 1
            bucket[tmp//sqn] -= 1

        deq[d[i]].append(i)
        tmp = deq[d[i]][-1] - deq[d[i]][0]
        lst[tmp] += 1
        bucket[tmp//sqn] += 1

    res += cal()

    for i in range(1,m):
        a,b = query[i]
        
        while a < pa:
            pa -= 1

            if deq[d[pa]]:
                tmp = deq[d[pa]][-1] - deq[d[pa]][0]
                lst[tmp] -= 1
                bucket[tmp//sqn] -= 1

            deq[d[pa]].appendleft(pa)
            tmp = deq[d[pa]][-1] - deq[d[pa]][0]
            lst[tmp] += 1
            bucket[tmp//sqn] += 1

        while pb < b:
            pb += 1

            if deq[d[pb]]:
                tmp = deq[d[pb]][-1] - deq[d[pb]][0]
                lst[tmp] -= 1
                bucket[tmp//sqn] -= 1

            deq[d[pb]].append(pb)
            tmp = deq[d[pb]][-1] - deq[d[pb]][0]
            lst[tmp] += 1
            bucket[tmp//sqn] += 1        
            
        while pa < a:
            tmp = deq[d[pa]][-1] - deq[d[pa]].popleft()
            lst[tmp] -= 1
            bucket[tmp//sqn] -= 1

            if deq[d[pa]]:
                tmp = deq[d[pa]][-1] - deq[d[pa]][0]
                lst[tmp] += 1
                bucket[tmp//sqn] += 1
            
            pa += 1 

        while b < pb:
            tmp = deq[d[pb]][-1] - deq[d[pb]][0]
            deq[d[pb]].pop()
            lst[tmp] -= 1
            bucket[tmp//sqn] -= 1

            if deq[d[pb]]:
                tmp = deq[d[pb]][-1] - deq[d[pb]][0]
                lst[tmp] += 1
                bucket[tmp//sqn] += 1

            pb -= 1

        res += cal()

    print(res)