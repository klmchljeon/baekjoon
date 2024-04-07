import sys
from collections import deque
input = sys.stdin.readline

dx = (-1,1,0,0)
dy = (0,0,-1,1)

m,n = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if d[i][j] == 1:
            visited[i][j] = 0
            queue.append((i,j))

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0<=nx<n and 0<=ny<m): continue
        if d[nx][ny]!=-1 and visited[nx][ny]==-1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

res = -1
flag = False
for i in range(n):
    for j in range(m):
        flag |= d[i][j]!=-1 and visited[i][j]==-1
        res = max(res,visited[i][j])

print(res if not flag else -1)