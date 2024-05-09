n,m = map(int,input().split())
d = [[0]*(n+1) for _ in range(2*n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    d[x][y] = 1

dp = [[-1]*(n+1) for _ in range(2*n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(i+1):
        if d[i][j] == 1: continue

        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])

        if j+1 <= i-1:
            dp[i][j] = max(dp[i][j], dp[i-1][j+1])

        if dp[i][j] != -1:
            dp[i][j] = max(dp[i][j], j)

for i in range(n+1,2*n+1):
    for j in range(2*n+1-i):
        if d[i][j] == 1:
            continue

        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        
        if True:
            dp[i][j] = max(dp[i][j], dp[i-1][j+1])

        if dp[i][j] != -1:
            dp[i][j] = max(dp[i][j], j)

print(dp[-1][0])