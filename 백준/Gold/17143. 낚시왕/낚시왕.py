#낚시왕 62:00
def sim():
    lst = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not d[i][j]:
                continue

            a = d[i][j]
            lo,di = move((i,j),*sh[a][:2])
            x,y = lo
            if lst[x][y] and sh[lst[x][y]][-1] > sh[a][-1]:
                continue

            lst[x][y] = a
            sh[a][1] = di

    for i in range(r):
        for j in range(c):
            d[i][j] = lst[i][j]

    return 

def move(loc,sp,dir):
    x,y = loc
    nx = x + sp*dx[dir]
    ny = y + sp*dy[dir]

    res = []
    div,mod = divmod(nx,r-1)
    if div%2:
        if nx!=x: dir = f(dir)
        res.append(r-mod-1)

    else:
        res.append(mod)

    div,mod = divmod(ny,c-1)
    if div%2:
        if ny!=y: dir = f(dir)
        res.append(c-mod-1)
    
    else:
        res.append(mod)

    return res,dir

f = lambda x:x+1 - 2*(x%2)

dx = (-1,1,0,0)
dy = (0,0,1,-1)

r,c,m = map(int,input().split())

d = [[0]*c for _ in range(r)]
sh = [[]]
for i in range(1,m+1):
    a,b,s,di,z = map(int,input().split())
    sh.append([s,di-1,z])
    d[a-1][b-1] = i

res = 0
for cal in range(c):
    for i in range(r):
        if d[i][cal]:
            num = d[i][cal]
            res += sh[num][2]

            d[i][cal] = 0
            break

    sim()

print(res)