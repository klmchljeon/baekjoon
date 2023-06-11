#구슬 탈출2
from collections import deque

def move(dir,x,y,mar=(0,0)):
    nx,ny = x,y
    while True:
        nx += dx[dir]
        ny += dy[dir]

        temp = d[nx][ny]
        if temp == '#' or (nx,ny) == mar:
            return (nx-dx[dir],ny-dy[dir])
        
        if temp == 'O':
            return False

def judge(dir,red,blue):
    div,mod = divmod(dir,2)
    if red[div^1] == blue[div^1]:
        if (red[div]>blue[div])^mod:
            return True

    return False

n,m = map(int,input().split())
d = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        temp = d[i][j]
        if temp == 'B':
            locB = (i,j)
            d[i][j] = '.'

        elif temp == 'R':
            locR = (i,j)
            d[i][j] = '.'

dx = (-1,1,0,0)
dy = (0,0,-1,1)

queue = deque([(locR,locB,0)])
while queue:
    r,b,t = queue.popleft()

    if t == 10:
        continue

    for i in range(4):
        rev = judge(i,r,b)
        if rev:
            nb = move(i,*b)
            if nb == False:
                continue
            nr = move(i,*r,nb)
            if nr == False:
                print(t+1)
                exit()

        else:
            nr = move(i,*r)
            if nr == False:
                nb = move(i,*b)
                if nb:
                    print(t+1)
                    exit()

                else:
                    continue

            nb = move(i,*b,nr)
            if nb == False:
                continue

        if nr == r and nb == b:
            continue
        queue.append([nr,nb,t+1])

print(-1)