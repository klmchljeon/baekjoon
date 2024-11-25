def move(q,loc,d):
    if q == 'F':
        x,y = loc
        nx = x + dx[d]
        ny = y + dy[d]

        if check((nx,ny)):
            return (nx,ny),d
        else:
            return loc,d
        
    if q == 'R':
        return loc,(d-1)%4
    else:
        return loc,(d+1)%4
    
def movez(loc,d):
    x,y = loc
    nx = x + dx[d]
    ny = y + dy[d]
    if check((nx,ny)):
        return (nx,ny),d
    else:
        return loc,(d+2)%4

def switch(loc):
    x,y = loc
    lst[x][y] = 'L'
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if check((nx,ny)) and lst[nx][ny] != 'S':
            lst[nx][ny] = 'L'

def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<n

def ah(loc):
    flag = False
    for z,_ in zom:
        flag |= z == loc

    x,y = loc
    return flag and lst[x][y] == 'O'

dx = (1,0,-1,0,-1,-1,1,1)
dy = (0,1,0,-1,-1,1,-1,1)

n = int(input())
a = input()
loc = (0,0)
d = 0

zom = []
lst = []
for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] == 'Z':
            tmp[j] = 'O'
            zom.append(((i,j),0))

    lst.append(tmp)

for i in range(len(a)):
    loc,d = move(a[i],loc,d)
    
    x,y = loc
    if lst[x][y] == 'S':
        switch((x,y))

    if ah(loc):
        print('Aaaaaah!')
        break

    tmp = []
    for z,idx in zom:
        z,idx=  movez(z,idx)
        tmp.append((z,idx))

    zom = tmp[:]
    
    if ah(loc):
        print('Aaaaaah!')
        break

else:
    print('Phew...')