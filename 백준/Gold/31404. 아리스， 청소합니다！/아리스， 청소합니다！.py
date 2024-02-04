dx = (-1,0,1,0)
dy = (0,1,0,-1)

h,w = map(int,input().split())
x,y,d = map(int,input().split())
a = [list(map(int,input())) for _ in range(h)]
b = [list(map(int,input())) for _ in range(h)]

tmp = 0
res = 0
dust = [[True]*w for _ in range(h)]
for _ in range(50000000):
    tmp += 1
    if dust[x][y]:
        dust[x][y] = False
        res = tmp
        d = (d + a[x][y])%4

    else:
        d = (d + b[x][y])%4

    nx = x + dx[d]
    ny = y + dy[d]

    if not (0<=nx<h and 0<=ny<w):
        break
    
    x,y = nx,ny

print(res)