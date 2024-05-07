from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
d = [input() for _ in range(n)]

visited = [[-1]*m for _ in range(n)]
visited[x1-1][y1-1] = 0

queue = deque([(x1-1,y1-1)])
while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<m): continue
        if visited[nx][ny] != -1: continue

        if d[nx][ny] == '0':
            visited[nx][ny] = visited[x][y]
            queue.appendleft((nx,ny))
        else:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

print(visited[x2-1][y2-1])