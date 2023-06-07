#채굴
import sys
from collections import deque
input = sys.stdin.readline

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(num):
    visit = [[False]*m for _ in range(n)]
    queue = deque([])

    for j in range(m):
        if d[0][j] <= num:
            visit[0][j] = True
            queue.append((0,j))

    for i in range(1,n):
        if d[i][0] <= num:
            visit[i][0] = True
            queue.append((i,0))

        if d[i][m-1] <= s:
            visit[i][m-1] = True
            queue.append((i,m-1))

    cnt = len(queue)
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and d[nx][ny] <= num:
                visit[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1

    return cnt >= k

n,m,k = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

s,e = 0,10**6
while s+1<e:
    mid = (s+e)//2

    if bfs(mid):
        e = mid

    else:
        s = mid

print(e)