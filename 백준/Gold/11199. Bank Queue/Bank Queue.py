#Bank Queue
import sys
from heapq import *
input = sys.stdin.readline

n,_ = map(int,input().split())
d = []
for _ in range(n):
    a,b = map(int,input().split())
    d.append((b,a))

d.sort()

res = []

for t,val in d:
    heappush(res,val)
    if t+1 < len(res):
        heappop(res)

print(sum(res))