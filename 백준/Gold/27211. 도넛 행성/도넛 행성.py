import sys
from collections import deque
input = sys.stdin.readline

def bfs(loc):
    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = (x + dx[i])%n
            ny = (y + dy[i])%m

            if not visited[nx][ny] and d[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny))

    return  

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and d[i][j] == 0:
            visited[i][j] = True
            bfs((i,j))
            cnt += 1

print(cnt)