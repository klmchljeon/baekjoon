from collections import deque

def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m

def fill(loc):
    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        tmp = []
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not check((nx,ny)): continue

            if d[nx][ny]:
                cnt += 1

            else:
                tmp.append((nx,ny))

        if cnt < 2:
            continue

        d[x][y] = True
        for i in tmp:
            queue.append(i)

def bfs(loc):
    min_ = [*loc]
    max_ = [*loc]

    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not check((nx,ny)): continue
            if not visited[nx][ny] and d[nx][ny]:
                visited[nx][ny] = True
                min_[0] = min(min_[0],nx)
                min_[1] = min(min_[1],ny)
                max_[0] = max(max_[0],nx)
                max_[1] = max(max_[1],ny)
                queue.append((nx,ny))

    x = max_[0] - min_[0] + 1
    y = max_[1] - min_[1] + 1
    return x,y

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m,k = map(int,input().split())
d = []
for _ in range(n):
    tmp = [i=='O' for i in input()]
    d.append(tmp)

queue = deque([])
for x in range(n):
    for y in range(m):
        if d[x][y]: continue

        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not check((nx,ny)): continue

            cnt += d[nx][ny]

        if cnt >= 2:
            d[x][y] = True
            fill((x,y))

res = 0
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and d[i][j]:
            visited[i][j] = True
            a,b = bfs((i,j))
            if min(a,b) > k:
                res += a*b
            
print(res)