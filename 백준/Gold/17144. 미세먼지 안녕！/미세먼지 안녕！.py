#미세먼지 안녕!
def blow():
    lst = [[0]*c for _ in range(r)]
    for x in loc:
        lst[x][0] = -1
    
    for x in range(r):
        for y in range(c):
            if d[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if not (0<=nx<r and 0<=ny<c): 
                        continue

                    if lst[nx][ny] == -1:
                        continue

                    lst[nx][ny] += d[x][y]//5
                    cnt += 1

                lst[x][y] += d[x][y] - cnt*(d[x][y]//5)

    return lst

def upair():
    x = loc[0]
    for i in range(x-1,0,-1):
        d[i][0] = d[i-1][0]

    for j in range(c-1):
        d[0][j] = d[0][j+1]

    for i in range(x):
        d[i][c-1] = d[i+1][c-1]

    for j in range(c-1,1,-1):
        d[x][j] = d[x][j-1]

    d[x][1] = 0

    return 

def downair():
    x = loc[1]
    for i in range(x+1,r-1):
        d[i][0] = d[i+1][0]

    for j in range(c-1):
        d[r-1][j] = d[r-1][j+1]

    for i in range(r-1,x,-1):
        d[i][c-1] = d[i-1][c-1]

    for j in range(c-1,1,-1):
        d[x][j] = d[x][j-1]

    d[x][1] = 0

    return 

dx = (-1,1,0,0)
dy = (0,0,-1,1)

r,c,t = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(r)]

for i in range(r):
    if d[i][0] == -1:
        loc = (i,i+1)
        break

for _ in range(t):
    b = blow()
    for i in range(r):
        for j in range(c):
            d[i][j] = b[i][j]

    upair()
    downair()

res = 2
for i in d:
    res += sum(i)

print(res)