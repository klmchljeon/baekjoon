import sys
from collections import deque
input = sys.stdin.readline

dx = (-1,-1,1,1,0,0)
dy = ((-1,0,-1,0,-1,1),(0,1,0,1,-1,1))

n,m,k = map(int,input().split())
lst = [[0]*m for _ in range(n)]
for _ in range(k):
    x,y = map(int,input().split())
    lst[x][y] = 1

visited = [[-1]*m for _ in range(n)]
visited[0][0] = 0

queue = deque([(0,0)])
while queue:
    x,y = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[x%2][i]

        if not (0<=nx<n and 0<=ny<m): continue
        if lst[nx][ny]: continue

        if visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

print(visited[n-1][m-1])