#벽 타기
from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

h,w = map(int,input().split())
st = [input() for _ in range(h)]

d = [[0]*w for _ in range(h)]
s,tar = [None]*2
for x in range(h):
    for y in range(w):
        if st[x][y] == '#':
            d[x][y] = -1
            continue

        if st[x][y] == 'S':
            s = (x,y)

        if st[x][y] == 'E':
            tar = (x,y)

        flag = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<h and 0<=ny<w): continue

            flag |= st[nx][ny]=='#'

        d[x][y] = int(flag)

x,y = s
visit = [[-1]*w for _ in range(h)]
visit[x][y] = 0

deq = deque([s])
while deq:
    x,y = deq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<h and 0<=ny<w): continue
        if d[nx][ny]==-1: continue 

        if d[nx][ny]&d[x][y]:
            if visit[nx][ny]==-1 or visit[nx][ny]>visit[x][y]:
                visit[nx][ny] = visit[x][y]
                deq.appendleft((nx,ny))

        elif visit[nx][ny] == -1:
            visit[nx][ny] = visit[x][y] + 1
            deq.append((nx,ny))

x,y = tar
print(visit[x][y])