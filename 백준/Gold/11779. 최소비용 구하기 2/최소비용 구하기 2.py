#거의 최단 경로
import sys
import math
import heapq
input = sys.stdin.readline
inf = math.inf

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,p = map(int,input().split())
    graph[u].append((v,p))

s,d = map(int,input().split())

dist = [[inf,[]] for _ in range(n+1)]
dist[s][0] = 0
dist[s][1].append(s)

heap = [(0,s)]
while heap:
    cost, node = heapq.heappop(heap)
    if dist[node][0] < cost:
        continue

    for i,c in graph[node]:
        if dist[i][0] > cost + c:
            dist[i][0] = cost + c
            dist[i][1] = dist[node][1] + [i]
            heapq.heappush(heap, (dist[i][0],i))

print(dist[d][0])
print(len(dist[d][1]))
print(*dist[d][1])