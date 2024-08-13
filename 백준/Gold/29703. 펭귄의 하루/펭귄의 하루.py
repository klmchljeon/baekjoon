from collections import deque
max_ = int(1e9)

def bfs(loc):
    x,y = loc
    visited = [[max_]*m for _ in range(n)]
    visited[x][y] = 0

    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not check((nx,ny)): continue
            if lst[nx][ny] == 'D': continue
            if visited[nx][ny] == max_:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    return visited

def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
lst = [list(input()) for _ in range(n)]

loc1,loc2 = None,None
loc3 = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'S':
            loc1 = (i,j)

        elif lst[i][j] == 'H':
            loc2 = (i,j)

        elif lst[i][j] == 'F':
            loc3.append((i,j))

visited1 = bfs(loc1)
visited2 = bfs(loc2)

res = max_
for i,j in loc3:
    res = min(res, visited1[i][j]+visited2[i][j])

print(res if res!=max_ else -1)