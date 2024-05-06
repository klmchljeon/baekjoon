from heapq import *
inf = int(1e9)

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
t,b,_,_ = map(int,input().split())
lst = [input() for _ in range(n)]

dist = [[inf]*m for _ in range(n)]
heap = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == '*':
            dist[i][j] = 0
            heappush(heap,(0,(i,j)))

while heap:
    cost,node = heappop(heap)
    x,y = node
    if dist[x][y] > cost:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<m): continue
        c = b+1 if lst[nx][ny] == '#' else 1
        if dist[nx][ny] > dist[x][y] + c:
            dist[nx][ny] = dist[x][y] + c
            heappush(heap,(dist[nx][ny],(nx,ny)))

flag = True
for i in range(n):
    for j in range(m):
        if dist[i][j] > t:
            print(i+1,j+1)
            flag = False

if flag:
    print(-1)