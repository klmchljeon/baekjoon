#거의 최단 경로
import heapq
import math
from sys import stdin
from collections import deque
input = stdin.readline
inf = math.inf

def dijkstra():
    result = [[] for _ in range(n)]
    dist = [inf]*n
    dist[s] = 0

    heap =[(0,s)]
    while heap:
        cost, node = heapq.heappop(heap)
        if dist[node] < cost:
            continue

        for i in graph[node]:
            if dist[i] == cost+graph[node][i]:
                result[i].append(node)

            if dist[i] > cost+graph[node][i]:
                dist[i] = cost+graph[node][i]
                result[i] = [node]
                heapq.heappush(heap,(dist[i],i))

    return result

def dijkstra2():
    dist = [inf]*n
    dist[s] = 0

    heap =[(0,s)]
    while heap:
        cost, node = heapq.heappop(heap)
        if dist[node] < cost:
            continue

        for i in graph[node]:
            if dist[i] > cost+graph[node][i]:
                dist[i] = cost+graph[node][i]
                heapq.heappush(heap,(dist[i],i))

    return dist[d]

def bfs():
    queue = deque([d])
    while queue:
        x = queue.popleft()

        for i in path[x]:
            try:
                del graph[i][x]
                queue.append(i)
            except:
                pass

    return

while True:
    n,m = map(int,input().split())
    if n==0: exit(0)

    s,d = map(int,input().split())
    graph = [dict() for _ in range(n)]
    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u][v] = p

    path = dijkstra()

    bfs()
    del path

    result = dijkstra2()
    if result == inf:
        print(-1)
    else:
        print(result)
    