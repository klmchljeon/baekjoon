import sys
from heapq import *
input = sys.stdin.readline
inf = int(1e18)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


s,t = 1,2
dp = [0]*(n+1)
dp[t] = 1

dist = [inf]*(n+1)
dist[t] = 0

heap = [(0,t)]
while heap:
    cost,node = heappop(heap)
    if dist[node] < cost:
        continue

    for nx,c in graph[node]:
        if dist[nx] > dist[node]:
            dp[nx] += dp[node]

        if dist[nx] > dist[node] + c:
            dist[nx] = dist[node] + c
            heappush(heap,(dist[nx],nx))

print(dp[1])