from collections import deque
max_ = int(1e9)

dx = (-1,-1,1,1)
dy = (-1,1,-1,1)

def crange(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m

def check(lst):
    cnt = 0
    for i in range(n):
        x,y = i,0
        p = lst[x][y][0]
        cnt += p
        while crange((x,y)):
            if lst[x][y][0] != p:
                return None

            x += dx[3]
            y += dy[3]

    for j in range(1,m):
        x,y = 0,j
        p = lst[x][y][0]
        cnt += p
        while crange((x,y)):
            if lst[x][y][0] != p:
                return None

            x += dx[3]
            y += dy[3]

    for i in range(n):
        x,y = i,0
        p = lst[x][y][1]
        cnt += p
        while crange((x,y)):
            if lst[x][y][1] != p:
                return None

            x += dx[1]
            y += dy[1]

    for j in range(1,m):
        x,y = n-1,j
        p = lst[x][y][1]
        cnt += p 
        while crange((x,y)):
            if lst[x][y][1] != p:
                return None

            x += dx[1]
            y += dy[1]
    
    return cnt

n,m = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

if n == 1:
    cnt = 0
    for i in lst[0]:
        cnt += i

    print(cnt)
    exit()

if m == 1:
    cnt = 0
    for i in lst:
        cnt += i[0]

    print(cnt)
    exit()

arr = []
for i in range(16):
    tmp = []
    for j in range(4):
        if i&(1<<j):
            tmp.append(1)
        else:
            tmp.append(0)

    arr.append(tmp)

res = max_
for p in arr:
    visited = [[False]*m for _ in range(n)]
    flip = [[[0,0] for _ in range(m)] for _ in range(n)]
    
    cnt = sum(p)

    m1 = (lst[0][0] + p[0]+p[1])%2
    m2 = (lst[0][1] + p[2]+p[3])%2
    if not (m1 == 0 and m2 == 0): continue

    flip[0][0] = [p[0],p[1]]
    flip[0][1] = [p[2],p[3]]

    visited[0][0] = True
    visited[0][1] = True

    queue = deque([(0,0),(0,1)])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not crange((nx,ny)): continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            k = lst[nx][ny]
            idx = (nx-x) != (ny-y)
            flip[nx][ny][idx] = flip[x][y][idx]
            
            k ^= flip[nx][ny][idx]
            flip[nx][ny][idx^1] = k
            queue.append((nx,ny))

    cnt = check(flip)
    if cnt != None:
        res = min(res,cnt)

print(res if res!=max_ else -1)