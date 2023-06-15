#배열 돌리기 4
max_ = int(1e9)

def rotate(idx):
    global arr
    r,c = loc[idx]
    for i in range(4):
        for x,y in move[idx][i]:
            v[x+r][y+c] = arr[x+r][y+c]

    for i in range(4):
        for x,y in move[idx][i]:
            nx = x + dx[i]
            ny = y + dy[i]
            arr[nx+r][ny+c] = v[x+r][y+c]

    return 

def sim(order):
    global arr
    arr = [d[i][:] for i in range(n)]
    for i in order:
        rotate(i)

    return cal()

def dfs():
    if len(tmp) == k:
        l.append(tmp[:])
        return 
    
    for i in range(k):
        if not i in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()

    return 

def cal():
    global arr
    res = max_
    for i in range(n):
        res = min(res,sum(arr[i]))

    return res

def pre(t):
    res = []

    lst = []
    s,e,p = -1,0,-1
    for _ in range(t):
        for y in range(s,e+1):
            lst.append((p,y))
        s-=1; e+=1; p-=1
    res.append(lst)

    lst = []
    s,e,p = -1,0,1
    for _ in range(t):
        for x in range(s,e+1):
            lst.append((x,p))
        s-=1; e+=1; p+=1
    res.append(lst)

    lst = []
    s,e,p = 0,1,1
    for _ in range(t):
        for y in range(s,e+1):
            lst.append((p,y))
        s-=1; e+=1; p+=1
    res.append(lst)

    lst = []
    s,e,p = 0,1,-1
    for _ in range(t):
        for x in range(s,e+1):
            lst.append((x,p))
        s-=1; e+=1; p-=1
    res.append(lst)

    return res

dx = (0,1,0,-1)
dy = (1,0,-1,0)

n,m,k = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

loc = []
move = []
for i in range(k):
    r,c,size = map(int,input().split())
    loc.append((r-1,c-1))
    move.append(pre(size))

l = []
tmp = []
dfs()

v = [[0]*m for _ in range(n)]

res = max_
for i in l:
    res = min(res,sim(i))

print(res)