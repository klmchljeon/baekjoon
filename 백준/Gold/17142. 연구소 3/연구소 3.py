#연구소 14:01
from collections import deque
max_ = 10000

def bfs(idx):
    visit = [[-1]*n for _ in range(n)]
    queue = deque([])
    
    for i in idx:
        x,y = loc[i]
        visit[x][y] = 0
        queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n): continue

            if visit[nx][ny]==-1 and d[nx][ny]!=1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx,ny))

    res = 0
    for i in range(n):
        for j in range(n):
            if d[i][j] == 0:
                if visit[i][j] == -1: return max_

                res = max(res,visit[i][j])

    return res

def dfs():
    if len(s) == m:
        lst.append(s[:])
        return 
    
    for i in range(k):
        if not s or s[-1] < i:
            s.append(i)
            dfs()
            s.pop()

    return 

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

loc = []
for i in range(n):
    for j in range(n):
        if d[i][j] == 2:
            loc.append((i,j))

k = len(loc)
lst = []
s = []
dfs()

res = max_
for i in lst:
    res = min(res,bfs(i))

print(res if res!=max_ else -1)