mod = int(1e9)+7

dx = (-1,0,0,-1,-1,0,-1)
dy = (0,-1,0,-1,0,-1,-1)
dz = (0,0,-1,0,-1,-1,-1)

s,a,b,c = map(int,input().split())
dp = [[[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)] for _ in range(s+1)]
dp[0][0][0][0] = 1

for k in range(1,s+1):
    for x in range(a+1):
        for y in range(b+1):
            for z in range(c+1):
                for i in range(7):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    nz = z + dz[i]
                    if not (nx>=0 and ny>=0 and nz>=0): continue

                    dp[k][x][y][z] = (dp[k][x][y][z] + dp[k-1][nx][ny][nz])%mod

print(dp[s][a][b][c])