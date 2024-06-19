from collections import deque

def check(dir,a,b):
    i,j = dir

    cx,cy = x,y
    for _ in range(a):
        cx += dx[i]
        cy += dy[i]
        if not (0<=cx<m and 0<=cy<n):
            return None,False
    
    i = (i+j)%4
    for _ in range(b):
        cx += dx[i]
        cy += dy[i]
        if not (0<=cx<m and 0<=cy<n):
            return None,False
        
    return (cx,cy),True

dx = (1,0,-1,0)
dy = (0,1,0,-1)

m,n,m1,m2 = map(int,input().split())
d = []
for _ in range(m):
    tmp = list(map(int,input().split()))
    d.append(tmp)

visited = [[False]*n for _ in range(m)]
queue = deque([])
for i in range(m):
    for j in range(n):
        if d[i][j] == 3:
            visited[i][j] = True
            queue.append((i,j,0))

while queue:
    x,y,t = queue.popleft()

    if d[x][y] == 4:
        print(t)
        break

    for i in range(4):
        for j in (-1,1):
            for v1,v2 in ((m1,m2),(m2,m1)):
                loc,b = check((i,j),v1,v2)
                if not b: continue

                nx,ny = loc
                if d[nx][ny] in (0,2): continue

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,t+1))
