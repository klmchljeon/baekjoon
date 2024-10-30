from heapq import *
inf = int(1e9)

def bt():
    if len(s) == n:
        idx.append(tuple(s))
        return 

    for i in range(n):
        if not i in s:
            s.append(i)
            bt()
            s.pop()

def check(d):
    for i in range(n-1):
        if lst[d[i]] > lst[d[i+1]]:
            return False

    return True

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
edge = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edge.append((a-1,b-1,c))

s = []
idx = []
bt()

dic = dict(zip(idx,range(len(idx))))

dist = [inf]*len(idx)
dist[0] = 0

heap = [(0,0)]
while heap:
    cost,node = heappop(heap)
    if cost > dist[node]: continue

    tmp = list(idx[node])
    for a,b,c in edge:
        tmp[a],tmp[b] = tmp[b],tmp[a]
        nx = dic[tuple(tmp)]
        tmp[a],tmp[b] = tmp[b],tmp[a]

        if dist[nx] > dist[node] + c:
            dist[nx] = dist[node] + c
            heappush(heap,(dist[nx],nx))

res = inf
for i in range(len(idx)):
    if check(idx[i]):
        res = min(res,dist[i])

print(res if res!=inf else -1)