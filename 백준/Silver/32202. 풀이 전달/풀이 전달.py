mod = int(1e9)+7

n = int(input())
dp = [[0]*2 for _ in range(n+1)]
dp[1][0] = 2
dp[1][1] = 1
for i in range(2,n+1):
    dp[i][0] = ((dp[i-1][0] + dp[i-1][1])*2)%mod
    dp[i][1] = (dp[i-1][0])%mod

print((dp[n][0]+dp[n][1])%mod)