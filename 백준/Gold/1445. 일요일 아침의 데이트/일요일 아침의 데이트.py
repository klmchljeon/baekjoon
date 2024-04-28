from heapq import *
inf = int(1e18)
max_ = int(1e4)

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [input() for _ in range(n)]

heap = []
end = None
lst = [[0]*m for _ in range(n)]
dist = [[inf]*m for _ in range(n)]

for x in range(n):
    for y in range(m):
        if d[x][y] == 'g':
            lst[x][y] = max_

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0<=nx<n and 0<=ny<m): continue
                if d[nx][ny] == '.':
                    lst[nx][ny] = 1

        elif d[x][y] == 'F':
            end = (x,y)
        
        elif d[x][y] == 'S':
            dist[x][y] = 0
            heap.append((0,(x,y)))

while heap:
    cost,loc = heappop(heap)
    x,y = loc
    if cost > dist[x][y]:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<n and 0<=ny<m): continue

        c = cost + lst[nx][ny]
        if dist[nx][ny] > c:
            dist[nx][ny] = c
            heappush(heap,(c,(nx,ny)))

x,y = end
res = divmod(dist[x][y],max_)
print(*res)