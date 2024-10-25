from collections import deque

def check(x,y,d):
    if not (0<=x<n and 0<=y<m): return False
    if visited[x][y][d] != -1 or lst[x][y] == '*': return False
    return True

dx = (-1,0,1,0)
dy = (0,-1,0,1)

m,n = map(int,input().split())
lst = [input() for _ in range(n)]

loc = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'C':
            loc.append((i,j))

res = []
for s in range(4):
    x,y = loc[0]
    visited = [[[-1]*4 for _ in range(m)] for _ in range(n)]
    visited[x][y][s] = 0
    queue = deque([(x,y,s,False)])
    
    while queue:
        x,y,d,b = queue.popleft()
        
        nx = x + dx[d]
        ny = y + dy[d]
        if check(nx,ny,d):
            visited[nx][ny][d] = visited[x][y][d] + b
            if b:
                queue.append((nx,ny,d,False))
            else:
                queue.appendleft((nx,ny,d,False))

        for i in (-1,1):
            idx = (d+i)%4

            if check(x,y,idx):
                visited[x][y][idx] = visited[x][y][d]
                queue.appendleft((x,y,idx,True))

    x,y = loc[1]
    res.append(min(visited[x][y]))

print(min(res))