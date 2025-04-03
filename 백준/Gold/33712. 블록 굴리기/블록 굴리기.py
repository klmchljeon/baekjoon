import sys
input = sys.stdin.readline

dx = (-1,1,0,0)
dy = (0,0,-1,1)
 
w = (
    (2,1,2,1),
    (1,2,1,1),
    (1,1,1,2)
)
 
p = (
    (1,1,2,2),
    (0,0,1,1),
    (2,2,0,0)
)

n,m,k = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

loc = None
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            loc = (i,j)

x,y = loc

dp = [[[[False]*3 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
dp[x][y][0][0] = True
for t in range(k):
    for x in range(n):
        for y in range(m):
            for d in range(3):
                if not dp[x][y][t][d]: continue                    

                for i in range(4):
                    nx = x + dx[i]*w[d][i]
                    ny = y + dy[i]*w[d][i]
                    nd = p[d][i]

                    if not (0<=nx<n-(nd==1) and 0<=ny<m-(nd==2)): continue
                    if not (lst[nx][ny]!=0 and lst[nx+(nd==1)][ny+(nd==2)]!=0): continue

                    dp[nx][ny][t+1][nd] = True

res = 0
for i in range(n):
    for j in range(m):
        if (i,j) == loc: continue
        res += dp[i][j][k][0]

print(res)