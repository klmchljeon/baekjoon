from collections import deque

dx = (-1,1,0,0,-1,-1,1,1)
dy = (0,0,-1,1,-1,1,-1,1)

n,m = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

visited = [[-1]*m for _ in range(n)]
queue = deque([])
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            visited[i][j] = 0
            queue.append((i,j))

while queue:
    x,y = queue.popleft()

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<m): continue
        if visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

res = 0
for i in range(n):
    for j in range(m):
        res = max(res,visited[i][j])

print(res)