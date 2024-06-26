import sys
from collections import deque
input = sys.stdin.readline
max_ = 1002
r,c = 310,310

def check(loc):
    x,y = loc
    return 0<=x<=r and 0<=y<=c

dx = (-1,1,0,0,0)
dy = (0,0,-1,1,0)

n = int(input())
d = [[max_]*(c+1) for _ in range(r+1)]
for _ in range(n):
    x,y,t = map(int,input().split())
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if not check((nx,ny)): continue
        d[nx][ny] = min(d[nx][ny],t)

visited = [[-1]*(c+1) for _ in range(r+1)]
visited[0][0] = 0

queue = deque([(0,0)])
while queue:
    x,y = queue.popleft()

    if d[x][y] == max_:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not check((nx,ny)): continue
        if visited[nx][ny] == -1 and d[nx][ny] > visited[x][y] + 1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

else:
    print(-1)