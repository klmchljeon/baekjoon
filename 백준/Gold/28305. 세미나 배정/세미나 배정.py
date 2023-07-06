#세미나 배정
from heapq import * 

def check(num):
    heap = []
    for i in d:
        if len(heap) < num:
            heappush(heap,max(t,i))
            continue

        tmp = heappop(heap)
        if tmp >= i:
            return False
        
        heappush(heap,max(tmp+t,i))

    return True

n,t = map(int,input().split())
d = list(map(int,input().split()))

d.sort()

s,e = 0,n
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid
    
    else:
        s = mid

print(e)