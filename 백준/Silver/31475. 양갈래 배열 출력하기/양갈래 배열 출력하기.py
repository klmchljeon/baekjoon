def fill(loc,dir,p,k):
    x,y = loc
    dir = (dir+p)%4
    
    x += dx[dir]
    y += dy[dir]
    while True:
        lst[x][y] = k
        k += 1

        nx = x + dx[dir]
        ny = y + dy[dir]

        if check((nx,ny)):
            x,y = nx,ny
            continue

        dir = (dir+p)%4
        nx = x + dx[dir]
        ny = y + dy[dir]

        if check((nx,ny)):
            x,y = nx,ny
            continue

        break
        
def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m and lst[x][y]==0

dx = (-1,0,1,0)
dy = (0,1,0,-1)

n,m = map(int,input().split())
di = "DLUR".find(input())

lst = [[0]*m for _ in range(n)]
st = [(n-1,m//2),(n//2,0),(0,m//2),(n//2,m-1)]

num = 1

x,y = st[di]
while 0<=x<n and 0<=y<m:
    lst[x][y] = num
    num += 1

    x += dx[di]
    y += dy[di]

x -= dx[di]
y -= dy[di]

fill((x,y),di,1,num)
fill((x,y),di,3,num)

for i in lst:
    print(*i)