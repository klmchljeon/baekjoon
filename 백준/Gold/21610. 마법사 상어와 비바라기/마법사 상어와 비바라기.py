dx = (0,-1,-1,-1,0,1,1,1)
dy = (-1,-1,0,1,1,1,0,-1)

def move(st,i,l):
    res = set()
    for x,y in st:
        nx = (x+dx[i]*l)%n
        ny = (y+dy[i]*l)%n

        res.add((nx,ny))

    return res

def check(loc):
    x,y = loc
    cnt = 0
    for i in range(1,8,2):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<n and 0<=ny<n):
            continue

        cnt += bool(d[nx][ny])

    return cnt

def produce(st):
    res = set()
    for i in range(n):
        for j in range(n):
            if (i,j) in st: continue

            if d[i][j] >= 2:
                d[i][j] -= 2
                res.add((i,j))

    return res

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]
query = []
for _ in range(m):
    dir,s = map(int,input().split())
    query.append((dir-1,s))

cloud = set()
for i in (n-1,n-2):
    for j in (0,1):
        cloud.add((i,j))

for dir,s in query:
    cloud = move(cloud,dir,s)
    for x,y in cloud:
        d[x][y] += 1

    for x,y in cloud:
        d[x][y] += check((x,y))

    cloud = produce(cloud)

res = 0
for i in d:
    for j in i:
        res += j

print(res)