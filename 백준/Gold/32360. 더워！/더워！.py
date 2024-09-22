from collections import deque

dx = (-1,1,0,0,0)
dy = (0,0,-1,1,0)

def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m

def find(loc):
    res = int(1e9)
    x,y = loc
    for k in visited[x][y]:
        if k != -1:
            res = min(res,k)

    return res

n,m = map(int,input().split())
k,c = map(int,input().split())
lst = [list(input()) for _ in range(n)]

s,e = None,None
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'S':
            s = (i,j)
        
        elif lst[i][j] == 'E':
            e = (i,j)

x,y = s
visited = [[[-1]*100 for _ in range(m)] for _ in range(n)]
visited[x][y][0] = 0

queue = deque([(x,y,0)])
while queue:
    x,y,u = queue.popleft()

    if (x,y) == e:
        print(find(e))
        break

    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if not check((nx,ny)): continue
        if lst[nx][ny] == '#': continue

        nu = None
        if lst[nx][ny] == 'H':
            nu = max(0,u-k)
        else:
            if u+c >= 100:
                continue

            nu = u+c

        if visited[nx][ny][nu] == -1:
            visited[nx][ny][nu] = visited[x][y][u] + 1
            queue.append((nx,ny,nu))

else:
    print(-1)
