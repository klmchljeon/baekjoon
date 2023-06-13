#캐슬 디펜스
from collections import deque

def bfs(sy):
    if tmp[n-1][sy] == 1:
        return (n-1,sy)

    res = []

    visit = [[0]*m for _ in range(n)]
    visit[n-1][sy] = 1

    queue = deque([(n-1,sy)])
    while queue:
        x,y = queue.popleft()

        if visit[x][y] == dis:
            break 

        if res and visit[x][y] >= visit[res[0][0]][res[0][1]]:
                break

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx and 0<=ny<m): continue
            if visit[nx][ny]: continue

            if tmp[nx][ny]: res.append((nx,ny))

            visit[nx][ny] = visit[x][y] + 1
            queue.append((nx,ny))

    if not res:
        return False

    res.sort(key = f)

    return res[0]

def sim(loc):
    cnt = 0
    for _ in range(n):
        st = set()
        for i in loc:
            tar = bfs(i)
            if tar:
                st.add(tar)

        for x,y in st:
            tmp[x][y] = 0

        cnt += len(st)

        for i in range(n-1,0,-1):
            tmp[i] = tmp[i-1][:]
        tmp[0] = [0]*m

    return cnt

def dfs():
    if len(s) == 3:
        lst.append(s[:])
        return 
    
    for i in range(m):
        if not s or s[-1] < i:
            s.append(i)
            dfs()
            s.pop()

    return 

f = lambda x:x[1]

dx = (-1,0,0)
dy = (0,-1,1)

n,m,dis = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

lst = []
s = []
dfs()

res = 0
for i in lst:
    tmp = [i[:] for i in d]
    res = max(res,sim(i))

print(res)