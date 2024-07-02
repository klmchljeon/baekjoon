from heapq import *

t = int(input())
for case in range(t):
    n = int(input())
    heap = list(map(int,input().split()))

    res = 0

    heapify(heap)
    while len(heap) > 1:
        a,b = heappop(heap), heappop(heap)
        
        c = a + b
        res += c
        heappush(heap,c)

    print(res)