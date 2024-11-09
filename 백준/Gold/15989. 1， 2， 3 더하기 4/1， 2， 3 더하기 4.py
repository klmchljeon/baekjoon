m = 10000
dp = [[0]*4 for _ in range(m+3)]
for i in (1,2,3):
    dp[i][i] = 1

for i in range(1,m):
    dp[i+1][1] += dp[i][1]
    dp[i+2][2] += dp[i][1] + dp[i][2]
    dp[i+3][3] += dp[i][1] + dp[i][2] + dp[i][3]

t = int(input())
for case in range(t):
    n = int(input())
    print(sum(dp[n]))