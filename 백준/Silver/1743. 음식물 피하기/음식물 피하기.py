#음식물 피하기 
from collections import deque

def bfs(loc):
    cnt = 1

    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<nx<=n and 0<ny<=m): continue

            if not visit[nx][ny] and d[nx][ny]:
                visit[nx][ny] = True
                
                queue.append((nx,ny))
                cnt += 1

    return cnt

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m,k = map(int,input().split())
d = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    x,y = map(int,input().split())
    d[x][y] = 1

visit = [[False]*(m+1) for _ in range(n+1)]

res = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if not visit[i][j] and d[i][j] == 1:
            visit[i][j] = True
            res = max(res, bfs((i,j)))

print(res)