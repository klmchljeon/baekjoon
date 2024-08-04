from heapq import *

n = int(input())
p = [0,0] + list(map(int,input().split()))
lst = [0] + list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
for i in range(2,n+1):
    graph[p[i]].append(i)

visited = [False]*(n+1)

x = 1
visited[x] = True
heap = [(-lst[x],1)]

res = 0
for _ in range(n):
    v,x = heappop(heap)
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            heappush(heap,(-lst[nx],nx))

    res += -v
    print(res)