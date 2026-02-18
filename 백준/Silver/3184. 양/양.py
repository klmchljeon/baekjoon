from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(loc):
    i,j = loc
    o,v = 0,0

    queue = deque([(i,j)])
    while queue:
        x,y = queue.popleft()
        if lst[x][y] == 'v':
            v += 1
        elif lst[x][y] == 'o':
            o += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<r and 0<=ny<c): continue
            if lst[nx][ny] == '#': continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))

    if o > v:
        return o,0
    else:
        return 0,v

r,c = map(int,input().split())
lst = [input() for _ in range(r)]

res = [0,0]

visited = [[False]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if lst[i][j] == '#': continue

        if not visited[i][j]:
            visited[i][j] = True
            o,v = bfs((i,j))
            res[0] += o
            res[1] += v

print(*res)