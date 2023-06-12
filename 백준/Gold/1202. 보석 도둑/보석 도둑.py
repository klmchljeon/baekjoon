#보석 도둑
import sys
from heapq import *
input = sys.stdin.readline

n,k = map(int,input().split())
d = []
for _ in range(n):
    m,v = map(int,input().split())
    d.append((m,v))

d.sort(reverse=1)

bag = [int(input()) for _ in range(k)]
bag.sort()

res = 0
heap = []
for i in bag:
    while d and d[-1][0] <= i:
        heappush(heap,-d.pop()[1])

    if heap:
        res += -heappop(heap)

print(res)