n,m,t = map(int,input().split())
dp = [[0,i] for i in range(t+1)]
for i in range(1,t+1):
    for p in (n,m):
        if i-p < 0: continue
        if dp[i][1] < dp[i-p][1]: continue

        if dp[i][1] == dp[i-p][1]:
            dp[i][0] = max(dp[i][0],dp[i-p][0]+1)

        else:
            dp[i] = [dp[i-p][0]+1,dp[i-p][1]]

print(*dp[t])