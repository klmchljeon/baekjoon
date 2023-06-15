#격자상의 경로
n,m,k = map(int,input().split())
dp = [[0]*(m+1) for _ in range(n+1)]

dp[1][1] = 1
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] += dp[i-1][j] + dp[i][j-1]

if not k:
    print(dp[n][m])
    exit()

x,y = divmod(k,m)
nx,ny = n-x,m-y
print(dp[x+1][y]*dp[nx+1][ny])