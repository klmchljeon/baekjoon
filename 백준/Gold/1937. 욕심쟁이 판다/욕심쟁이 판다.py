#욕심쟁이 판다
import sys
sys.setrecursionlimit(30000)

def dfs(loc):
    x,y = loc
    if dp[x][y]:
        return dp[x][y]

    tmp = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<n): continue

        if d[nx][ny] > d[x][y]:

            tmp = max(tmp,dfs((nx,ny))+1)

    dp[x][y] = tmp
    return tmp

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            dfs((i,j))

res = 0
for i in range(n):
    for j in range(n):
        res = max(res,dp[i][j])

print(res)