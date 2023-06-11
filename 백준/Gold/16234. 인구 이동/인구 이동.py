#인구 이동
from collections import deque

dx = (0,0,-1,1)
dy = (-1,1,0,0)

def conv(lst):
    s = 0
    for x,y in lst:
        s += d[x][y]

    s //= len(lst)

    for x,y in lst:
        d[x][y] = s

    return 

def bfs(loc):
    res = [loc]
    
    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue

            if visit[nx][ny]:
                continue

            if not (l <= abs(d[x][y]-d[nx][ny]) <= r):
                continue

            visit[nx][ny] = True
            queue.append((nx,ny))
            res.append((nx,ny))

    return res 

n,l,r = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
while True:
    visit = [[False]*n for _ in range(n)]
    group = []
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = True
                tmp = bfs((i,j))
                if len(tmp) > 1:
                    group.append(tmp)

    if not group: 
        break

    for i in group:
        conv(i)

    cnt += 1

print(cnt)