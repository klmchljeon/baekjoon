max_ = 100

dx = (1,0,-1,0)
dy = (0,1,0,-1)

lst = [['#']*(max_+1) for _ in range(max_+1)]
x,y = 50,50
lst[x][y] = '.'

n = int(input())
st = list(input())
dir = 0
bx = [x,x+1]
by = [y,y+1]
for i in range(n):
    if st[i] == 'F':
        x = x + dx[dir]
        y = y + dy[dir]
    
    elif st[i] == 'L':
        dir = (dir+1)%4

    elif st[i] == 'R':
        dir = (dir-1)%4

    bx[0] = min(bx[0],x)
    bx[1] = max(bx[1],x+1)
    by[0] = min(by[0],y)
    by[1] = max(by[1],y+1)
    lst[x][y] = '.'

for i in range(*bx):
    for j in range(*by):
        print(lst[i][j], end = '')
    print()