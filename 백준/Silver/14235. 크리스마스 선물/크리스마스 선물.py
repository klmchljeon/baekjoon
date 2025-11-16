from heapq import *

n = int(input())
heap = []
for _ in range(n):
    a,*lst = map(int,input().split())
    if a == 0:
        if not heap:
            print(-1)
        else:
            print(-heappop(heap))

    else:
        for i in lst:
            heappush(heap,-i)