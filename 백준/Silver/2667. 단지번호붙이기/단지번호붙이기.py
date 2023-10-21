from collections import deque

n = int(input())
d = [input() for _ in range(n)]

def bfs(loc):
    res = 0

    queue = deque([loc])
    while queue:
        x,y = queue.popleft()
        res += 1

        nx,ny = x-1,y
        if (0<=nx<n and 0<=ny<n):
            if d[nx][ny] == '1' and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx,ny))

        nx,ny = x+1,y
        if (0<=nx<n and 0<=ny<n):
            if d[nx][ny] == '1' and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx,ny))

        nx,ny = x,y-1
        if (0<=nx<n and 0<=ny<n): 
            if d[nx][ny] == '1' and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx,ny))

        nx,ny = x,y+1
        if (0<=nx<n and 0<=ny<n): 
            if d[nx][ny] == '1' and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx,ny))

    return res

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