from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(loc,color):
    x,y = loc
    cnt = 1
    
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<m and 0<=ny<n): continue
            if not (lst[nx][ny] == color): continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx,ny))

    return cnt

n,m = map(int,input().split())
lst = []
for _ in range(m):
    tmp = input()
    lst.append([i=='B' for i in tmp])

visited = [[False]*n for _ in range(m)]
res = [0,0]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            p = bfs((i,j),lst[i][j])
            res[lst[i][j]] += p**2

print(*res)