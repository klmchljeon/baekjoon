#소년 점프
from collections import deque
inf = 25000

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(loc):
    sx,sy = loc
    sx-=1
    sy-=1

    visit = [[-1]*m for _ in range(n)]
    visit[sx][sy] = 0

    queue = deque([(sx,sy)])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == -1 and not d[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx,ny))

    return visit

n,m = map(int,input().split())
d = [list(map(int,input())) for _ in range(n)]

l = [map(int,input().split()) for _ in range(3)]

v = [bfs(i) for i in l]

res = [inf,0]
for i in range(n):
    for j in range(m):
        if d[i][j]: continue

        tmp = 0
        flag = False
        for k in range(3):
            flag |= v[k][i][j] == -1 
            tmp = max(tmp, v[k][i][j])
        if flag: continue
        
        if res[0] > tmp:
            res = [tmp,1]

        elif res[0] == tmp:
            res[1] += 1

if res[0] == inf:
    print(-1)
else:
    print(*res,sep='\n')