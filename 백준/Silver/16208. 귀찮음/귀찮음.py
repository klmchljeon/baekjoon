from heapq import *

n = int(input())
heap = list(map(int,input().split()))
heapify(heap)

res = 0
while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    res += a*b
    heappush(heap,a+b)

print(res)