def cal(loc):
    res = -1
    for di in d:
        res = max(res,conv(loc,di))

    return res

def conv(loc,di):
    x,y = loc
    dx,dy = di

    res = -1
    p = 0
    cnt = 0
    while check((x,y)):
        p += lst[x][y] * (10**cnt)
        
        tmp = int(p**0.5)
        if p == tmp**2:
            res = p

        x += dx
        y += dy
        cnt += 1

    return res

def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m

d = []
for i in range(-8,9):
    for j in range(-8,9):
        if i or j:
            d.append((i,j))

n,m = map(int,input().split())
lst = [list(map(int,input())) for _ in range(n)]

res = -1
for i in range(n):
    for j in range(m):
        res = max(res,cal((i,j)))

print(res)