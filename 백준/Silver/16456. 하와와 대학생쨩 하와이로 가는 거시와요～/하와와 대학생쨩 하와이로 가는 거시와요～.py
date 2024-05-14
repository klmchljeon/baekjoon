mod = int(1e9) + 9

n = int(input())
dp = [[0]*2 for i in range(n+1)]
dp[1][0] = 1

for i in range(2,n+1):
    dp[i][0] = sum(dp[i-1])%mod
    dp[i][1] = dp[i-2][0]%mod

print(sum(dp[n])%mod)