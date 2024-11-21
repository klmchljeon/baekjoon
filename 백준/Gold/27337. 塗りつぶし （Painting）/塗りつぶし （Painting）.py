dx = (-1,1,0,0)
dy = (0,0,-1,1)

def find(loc):
    x,y = loc
    if parent[x][y] == loc: return loc
    parent[x][y] = find(parent[x][y])
    return parent[x][y]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        px,py = pa
        x,y = pb

    elif pa > pb:
        px,py = pb
        x,y = pa

    else:
        return 

    parent[x][y] = (px,py)
    area[px][py] += area[x][y]   

h,w = map(int,input().split())
lst = []
for _ in range(h):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

parent = [[(i,j) for j in range(w)] for i in range(h)]
area = [[1]*w for _ in range(h)]

for x in range(h):
    for y in range(w):
        p = find((x,y))
        if p == (x,y):
            pass

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<h and 0<=ny<w): continue

            if lst[nx][ny] == lst[x][y]:
                merge((nx,ny),(x,y))

dic = dict()
cnt = []
d = []
for x in range(h):
    for y in range(w):
        p = find((x,y))
        if not p in dic:
            x,y = p
            dic[p] = len(dic)
            cnt.append(area[x][y])
            d.append((x,y))

n = len(d)
graph = [set() for _ in range(n)]
for x in range(h):
    for y in range(w):
        for i in (0,2):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<h and 0<=ny<w): continue

            a = find((x,y))
            b = find((nx,ny))
            if a != b:
                graph[dic[a]].add(dic[b])
                graph[dic[b]].add(dic[a])

res = 0
for a in range(n):
    x,y = d[a]
    ax = area[x][y]

    c = dict()
    for b in graph[a]:
        nx,ny = d[b]
        color = lst[nx][ny]
        if not color in c:
            c[color] = 0

        c[color] += area[nx][ny]

    tmp = 0
    for i in c:
        tmp = max(tmp,c[i])

    res = max(res,ax+tmp)

print(res)