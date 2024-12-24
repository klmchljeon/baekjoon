mod = int(1e5)

n,m = map(int,input().split())
dp = [[[0]*4 for _ in range(m)] for _ in range(n)]
for i in range(n):
    dp[i][0][0] = 1
for j in range(m):
    dp[0][j][1] = 1

for i in range(1,n):
    for j in range(1,m):
        dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][2])%mod
        dp[i][j][1] = (dp[i][j-1][1] + dp[i][j-1][3])%mod
        dp[i][j][2] = dp[i-1][j][1]
        dp[i][j][3] = dp[i][j-1][0]

print(sum(dp[-1][-1])%mod)