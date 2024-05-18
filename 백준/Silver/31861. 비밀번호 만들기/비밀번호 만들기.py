mod = int(1e9) + 7

n,m = map(int,input().split())
dp = [[0]*26 for _ in range(m)]
for j in range(26):
    dp[0][j] = 1

for i in range(1,m):
    for j in range(26):
        for k in range(26):
            if abs(j-k) >= n:
                dp[i][j] = (dp[i][j] + dp[i-1][k])%mod

res = sum(dp[m-1])%mod
print(res)