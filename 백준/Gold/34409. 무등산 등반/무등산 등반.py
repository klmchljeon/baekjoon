from heapq import *
inf = int(1e10)
 
dx = (-1,1,0,0)
dy = (0,0,-1,1)
 
def cal(p,q):
    x,y = p
    nx,ny = q
    if abs(lst[x][y] - lst[nx][ny]) > c:
        return -1
    
    if lst[x][y] < lst[nx][ny]:
        return (lst[nx][ny] - lst[x][y])*a
 
    if lst[x][y] > lst[nx][ny]:
        return (lst[x][y] - lst[nx][ny])*b
 
    return 1
 
n,m = map(int,input().split())
x,y = map(int,input().split())
x-=1; y-=1
a,b,c = map(int,input().split())
 
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)
 
v = -1
loc = None
for i in range(n):
    for j in range(m):
        if v < lst[i][j]:
            v = lst[i][j]
            loc = (i,j)
 
dist = [[inf]*m for _ in range(n)]
dist[x][y] = 0
 
heap = [(0,(x,y))]
while heap:
    cost,node = heappop(heap)
    x,y = node
    if dist[x][y] < cost: continue
 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
 
        if not (0<=nx<n and 0<=ny<m): continue
        
        nc = cal(node,(nx,ny))
        if nc == -1: continue
 
        if dist[nx][ny] > dist[x][y] + nc:
            dist[nx][ny] = dist[x][y] + nc
            heappush(heap,(dist[nx][ny],(nx,ny)))
 
x,y = loc
print(dist[x][y] if dist[x][y]!=inf else -1)
