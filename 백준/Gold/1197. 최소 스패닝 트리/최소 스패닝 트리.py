import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())
visit = [False]*(v+1)
d = [[] for _ in range(v+1)]
heap = [[0,1]]
for _ in range(e):
    a,b,c = map(int,input().split())
    d[a].append([c,b])
    d[b].append([c,a])

result = 0
count = 0
while heap:
    w,s = heapq.heappop(heap)
    if not visit[s]:
        visit[s] = True
        result += w
        count += 1
        for i in d[s]:
            heapq.heappush(heap, i)

print(result)