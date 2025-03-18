import sys
from collections import deque
from heapq import *
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

s,e = map(int,input().split())

dist = [[-1,[]] for _ in range(n+1)]
dist[s][0] = 0

heap = [(0,s)]
while heap:
    cost,node = heappop(heap)
    cost = -cost
    if cost < dist[node][0]: continue

    for nx,c in graph[node]:
        tmp = cost + c
        if dist[nx][0] == tmp:
            dist[nx][1].append(node)

        elif dist[nx][0] < tmp:
            dist[nx] = [tmp,[node]]
            heappush(heap,(-tmp,nx))

res = 0

visited = [False]*(n+1)
visited[e] = True

queue = deque([e])
while queue:
    x = queue.popleft()

    res += len(dist[x][1])
    for nx in dist[x][1]:
        if not visited[nx]:
            visited[nx] = True
            queue.append(nx)

print(dist[e][0])
print(res)