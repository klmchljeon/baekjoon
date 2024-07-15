def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m

def dfs(loc):
    x,y = loc
    p = lst[x][y]
    
    mx = [n,0]
    my = [m,0]
    
    stack = [loc]
    while stack:
        x,y = stack.pop()
        
        mx[0] = min(mx[0], x)
        mx[1] = max(mx[1], x + 1)
        my[0] = min(my[0], y)
        my[1] = max(my[1], y + 1)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not check((nx,ny)): continue
            
            if not visited[nx][ny] and lst[nx][ny] == p:
                visited[nx][ny] = True
                stack.append((nx,ny))

    return mx,my

def judge(lx,ly):
    p = lst[lx[0]][ly[0]]
    for i in range(*lx):
        for j in range(*ly):
            if lst[i][j] != p:
                return False
            
    return True

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
lst = [input() for _ in range(n)]

visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            if not judge(*dfs((i,j))):
                print("BaboBabo")
                exit()

print("dd")