#1, 2, 3 더하기 5
mod = 1000000009
m = 100000

dp = [[0]*4 for _ in range(m+1)]

for i in range(1,4):
    dp[i][i] = 1

for i in range(1,m+1):
    for j in range(1,4):
        for k in range(1,4):
            if j==k: continue
            dp[i][j] += dp[i-j][k]

        dp[i][j] %= mod

t = int(input())
for case in range(t):
    n = int(input())
    print(sum(dp[n])%mod)