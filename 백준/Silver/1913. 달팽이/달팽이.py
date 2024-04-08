def f(num):
    for i in range(n):
        for j in range(n):
            if d[i][j] == num:
                return i+1,j+1

dx = (0,1,0,-1)
dy = (1,0,-1,0)

n = int(input())
m = int(input())

d = [[0]*n for _ in range(n)]
x,y = n//2,n//2
d[x][y] = 1
x -= 1
dir = 0
for i in range(2,n**2):
    d[x][y] = i

    x += dx[dir]
    y += dy[dir]

    ndir = (dir+1)%4
    tx = x + dx[ndir]
    ty = y + dy[ndir]
    if not d[tx][ty]:
        dir = ndir

d[0][0] = n**2
for i in d:
    print(*i)
print(*f(m))