import sys
from collections import deque
input = sys.stdin.readline

dx = (-1,1,0,0)
dy = (0,0,-1,1)

m,n = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]

queue = deque([])
cnt = n*m
for i in range(n):
    for j in range(m):
        t = d[i][j]
        if t == 1:
            queue.append((i,j,0))
            visit[i][j] = True
        elif t == -1:
            cnt -= 1

while queue:
    x,y,t = queue.popleft()
    cnt -= 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and d[nx][ny] == 0:
            visit[nx][ny] = True
            queue.append((nx,ny,t+1))

print(-1 if cnt else t)