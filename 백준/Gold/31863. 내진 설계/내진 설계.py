from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(input()) for _ in range(n)]

loc = None
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if d[i][j] == '@':
            loc = (i,j)
        
        elif d[i][j] == '#':
            visited[i][j] -= 2

queue = deque([])
for i in range(4):
    x,y = loc
    for k in (1,2):
        nx = x + k*dx[i]
        ny = y + k*dy[i]
        if not (0<=nx<n and 0<=ny<m): break
        if d[nx][ny] == '|': break

        if d[nx][ny] == '*':
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

        elif d[nx][ny] == '#':
            if visited[nx][ny] < 0:
                visited[nx][ny] += 1

            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<n and 0<=ny<m): continue
        if d[nx][ny] == '|': continue

        if d[nx][ny] == '*':
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

        elif d[nx][ny] == '#':
            if visited[nx][ny] < 0:
                visited[nx][ny] += 1

            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

res = [0,0]
for i in range(n):
    for j in range(m):
        if d[i][j] in '*#':
            if visited[i][j] == 1:
                res[0] += 1

            else:
                res[1] += 1

print(*res)