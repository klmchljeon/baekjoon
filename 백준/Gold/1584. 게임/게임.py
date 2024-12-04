from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n = 500
lst = [[0]*(n+1) for _ in range(n+1)]

a = int(input())
for _ in range(a):
    x1,y1,x2,y2 = map(int,input().split())
    if x1>x2: x1,x2 = x2,x1
    if y1>y2: y1,y2 = y2,y1
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            lst[i][j] = 1

b = int(input())
for _ in range(b):
    x1,y1,x2,y2 = map(int,input().split())
    if x1>x2: x1,x2 = x2,x1
    if y1>y2: y1,y2 = y2,y1
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            lst[i][j] = -1


visited = [[-1]*(n+1) for _ in range(n+1)]
visited[0][0] = 0

queue = deque([(0,0)])
while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<=n and 0<=ny<=n): continue
        if lst[nx][ny] == -1: continue

        if visited[nx][ny] == -1:
            if lst[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]
                queue.appendleft((nx,ny))

            else:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

print(visited[n][n])