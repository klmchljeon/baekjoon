from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(loc):
    res = 0

    queue = deque([loc])
    while queue:
        x,y = queue.popleft()
        res += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n): continue

            if d[nx][ny] == '1' and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx,ny))

    return res

n = int(input())
d = [input() for _ in range(n)]

visit = [[False]*n for _ in range(n)]

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if d[i][j]=='1' and not visit[i][j]:
            visit[i][j] = True
            cnt += 1
            ans.append(bfs((i,j)))

    
print(cnt)
print(*sorted(ans),sep='\n')