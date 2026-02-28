import sys
from heapq import *
input = sys.stdin.readline
inf = int(1e9)

t = int(input())
for case in range(t):
    n,m,k = map(int,input().split())
    s,g,h = map(int,input().split())
    if g > h: g,h = h,g

    p = 0
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        if (a,b) == (g,h): p = d

        graph[a].append((b,d))
        graph[b].append((a,d))

    lst = [int(input()) for _ in range(k)]
    
    dist = [inf]*(n+1)
    dist[s] = 0

    heap = [(0,s)]
    while heap:
        cost,node = heappop(heap)
        if dist[node] < cost: continue

        for nx,c in graph[node]:
            if dist[nx] > dist[node] + c:
                dist[nx] = dist[node] + c
                heappush(heap,(dist[nx],nx))

    distg = [inf]*(n+1)
    distg[g] = 0

    heap = [(0,g)]
    while heap:
        cost,node = heappop(heap)
        if distg[node] < cost: continue

        for nx,c in graph[node]:
            if distg[nx] > distg[node] + c:
                distg[nx] = distg[node] + c
                heappush(heap,(distg[nx],nx))

    disth = [inf]*(n+1)
    disth[h] = 0

    heap = [(0,h)]
    while heap:
        cost,node = heappop(heap)
        if disth[node] < cost: continue

        for nx,c in graph[node]:
            if disth[nx] > disth[node] + c:
                disth[nx] = disth[node] + c
                heappush(heap,(disth[nx],nx))

    res = []
    for i in lst:
        f1 = dist[g] + p + disth[i] == dist[i]
        f2 = dist[h] + p + distg[i] == dist[i]
        if f1 or f2:
            res.append(i)

    print(*sorted(res))