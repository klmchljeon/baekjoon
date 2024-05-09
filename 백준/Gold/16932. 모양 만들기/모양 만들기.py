from collections import deque

def bfs(loc,a):
    tmp = [loc]
    
    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m): continue
            if not visited[nx][ny] and d[nx][ny] == 1:
                visited[nx][ny] = True
                tmp.append((nx,ny))
                queue.append((nx,ny))

    k = len(tmp)
    for x,y in tmp:
        cnt[x][y] = (k,a)

    return 

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

idx = 0
cnt = [[(0,-1)]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if d[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            bfs((i,j),idx)
            idx += 1

res = 0
for x in range(n):
    for y in range(m):
        if d[x][y] == 1: continue

        st = set()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m): continue
            st.add(cnt[nx][ny])

        p = 1
        for i,_ in st:
            p += i

        res = max(res,p)

print(res)