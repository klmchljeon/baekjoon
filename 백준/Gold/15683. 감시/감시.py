#감시 26:34
def cal(lst):
    cnt = 0

    cctv = []
    for i in range(k):
        tmp = loc[i][1][:]
        for _ in range(lst[i]):
            tmp = map(f,tmp)

        cctv.append((loc[i][0],list(tmp)))

    visit = [[False]*m for _ in range(n)]
    for l,dir in cctv:
        x,y = l
        for i in dir:
            a = 0
            while True:
                nx = x + a*dx[i]
                ny = y + a*dy[i]
                if not (0<=nx<n and 0<=ny<m): break

                if d[nx][ny] == 6: break

                if not visit[nx][ny]:
                    visit[nx][ny] = True

                    if not d[nx][ny]:
                        cnt += 1

                a += 1

    return cnt

def dfs():
    global res
    if len(s)==len(loc):
        res = max(res,cal(s))
        return 
    
    for i in range(4):
        s.append(i)
        dfs()
        s.pop()

    return 

f = lambda x:(x+1)%4

t = (None,[0],[0,2],[0,1],[0,1,2],[0,1,2,3])

dx = (-1,0,1,0)
dy = (0,-1,0,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

q = 0
loc = []
for i in range(n):
    for j in range(m):
        if d[i][j]: q += 1

        if 1 <= d[i][j] <= 5:
            loc.append([(i,j),t[d[i][j]]])

k = len(loc)

res = 0
s = []
dfs()

print(n*m-q-res)