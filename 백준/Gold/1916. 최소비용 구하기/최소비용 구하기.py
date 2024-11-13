import sys
import heapq
input = sys.stdin.readline
inf = int(1e18)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

s,e = map(int,input().split())

dist = [inf]*(n+1)
dist[s] = 0

heap = [(0,s)]
while heap:
    cost,node = heapq.heappop(heap)
    if dist[node] < cost: continue
    #dist[node] == cost는 보장됨

    for nx,c in graph[node]:
        if dist[nx] > cost + c:
            dist[nx] = cost + c
            heapq.heappush(heap,(dist[nx],nx))

print(dist[e])