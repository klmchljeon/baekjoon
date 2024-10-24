from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,k = map(int,input().split())
lst = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] != 0:
            visited[i][j] = tmp[j]
            lst.append((tmp[j],(i,j),0))

s,a,b = map(int,input().split())
queue = deque(sorted(lst))
while queue:
    num,loc,t = queue.popleft()

    if t == s: break

    x,y = loc
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<n): continue
        if not visited[nx][ny]:
            visited[nx][ny] = num
            queue.append((num,(nx,ny),t+1))

print(visited[a-1][b-1])