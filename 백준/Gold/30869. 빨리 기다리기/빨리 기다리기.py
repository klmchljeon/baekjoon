import sys
from heapq import *
input = sys.stdin.readline
inf = int(1e9)

n,m,k = map(int,input().split())
d = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t,g = map(int,input().split())
    d[s].append((e,t,g))

dis = [inf]*(n+1)
dis[1] = 0

heap = [(0,0,1)]
while heap:
    c,p,x = heappop(heap)
    p = -p
    if dis[x] < c: continue

    s = dis[x]
    for nx,t,g in d[x]:
        tmp = s%g
        if tmp: tmp = g-tmp

        if dis[nx] > s + tmp+t:
            dis[nx] = s + tmp+t
            heappush(heap,(dis[nx],-p,nx))

        if p < k and dis[nx] > s + t:
            dis[nx] = s + t
            heappush(heap,(dis[nx],-(p+1),nx))

res = dis[n]
print(res if res!=inf else -1)