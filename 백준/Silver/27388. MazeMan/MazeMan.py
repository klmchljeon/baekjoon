from collections import deque

def bfs(loc):
    queue = deque([loc])
    flag = False
    cnt = 1
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m): continue
            if not visited[nx][ny] and lst[nx][ny]!='X':
                visited[nx][ny] = True
                if lst[nx][ny] in ' .':
                    cnt += lst[nx][ny] == '.'
                    queue.append((nx,ny))
                else:
                    flag = True

    return 0 if flag else cnt

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
lst = [input() for _ in range(n)]

visited = [[False]*m for _ in range(n)]
res = [0,0]
for i in range(1,n-1):
    for j in range(1,m-1):
        if not visited[i][j] and lst[i][j] == '.':
            visited[i][j] = True
            tmp = bfs((i,j))
            if tmp:
                res[1] += tmp
            else:
                res[0] += 1

print(*res)