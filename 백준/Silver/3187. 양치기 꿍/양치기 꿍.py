#양치기 꿍 
from collections import deque

def bfs(loc):
    sx,sy = loc
    visit[sx][sy] = True

    ck,cv = 0,0
    queue = deque([loc])
    while queue:
        x,y = queue.popleft()
        if d[x][y] == 'k': ck += 1
        elif d[x][y] == 'v': cv += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c and not visit[nx][ny] and d[nx][ny] != '#':
                visit[nx][ny] = True
                queue.append((nx,ny))

    if ck > cv: 
        return ck,0
    else: 
        return 0,cv

dx = (-1,1,0,0)
dy = (0,0,-1,1)

r,c = map(int,input().split())
d = [input() for _ in range(r)]
visit = [[False]*c for _ in range(r)]

k,v = 0,0
for i in range(r):
    for j in range(c):
        if not visit[i][j] and d[i][j] != '#':
            tmp = bfs((i,j))
            k += tmp[0]
            v += tmp[1]

print(k,v)