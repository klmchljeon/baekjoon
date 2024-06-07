max_ = int(1e5)
m = int(1e3)

n,k = map(int,input().split())
d = [0]+list(map(int,input().split()))

dp = [[0] + [m]*(max_) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(max_):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        
        if dp[i][j] != m:
            dp[i][j+d[i]] = min(dp[i][j+d[i]], dp[i-1][j]+1)

res = dp[n][k]
print(res if res!=m else -1)