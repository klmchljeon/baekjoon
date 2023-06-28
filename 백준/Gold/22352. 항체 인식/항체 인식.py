from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
fir = [list(map(int,input().split())) for _ in range(n)]
sec = [list(map(int,input().split())) for _ in range(n)]

c1 = [[False]*m for _ in range(n)]
flag = None
loc = None
cnt = 0
for i in range(n):
    for j in range(m):
        if fir[i][j] != sec[i][j]:
            if flag == None:
                flag = [fir[i][j], sec[i][j]]
                loc = (i,j)

            else:
                if flag[0]!=fir[i][j] or flag[1]!= sec[i][j]:
                    print('NO')
                    exit()

            cnt += 1
            c1[i][j] = True

if flag == None:
    print('YES')
    exit()

x,y = loc
v1 = [[False]*m for _ in range(n)]
v1[x][y] = True

queue = deque([loc])
cnt -= 1
while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<m): continue
        if not v1[nx][ny] and c1[nx][ny]:
            v1[nx][ny] = True
            cnt -= 1
            queue.append((nx,ny))

if cnt:
    print('NO')
    exit()

col = flag[0]

queue = deque([])
for i in range(n):
    for j in range(m):
        if v1[i][j]:
            queue.append((i,j))

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<m): continue
        if not v1[nx][ny] and fir[nx][ny]==col:
            print('NO')
            exit()

print('YES')