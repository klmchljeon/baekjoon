import sys
from heapq import *
input = sys.stdin.readline

n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
b = [0] + list(map(int,input().split()))

heapn = [(a[i],i) for i in range(1,n+1)]
heapify(heapn)

heapm = [(b[i],i) for i in range(1,m+1)]
heapify(heapm)

k = int(input())
for _ in range(k):
    q,*order = input().split()
    if q == 'U':
        x,y = map(int,order)
        if x <= n:
            heappush(heapn,(y,x))
            a[x] = y
        else:
            x -= n
            heappush(heapm,(y,x))
            b[x] = y

    else:
        while True:
            val,idx = heappop(heapn)
            if a[idx] == val:
                break

        p = idx
        heappush(heapn,(val,idx))

        while True:
            val,idx = heappop(heapm)
            if b[idx] == val:
                break

        q = idx
        heappush(heapm,(val,idx))
        print(p,q+n)