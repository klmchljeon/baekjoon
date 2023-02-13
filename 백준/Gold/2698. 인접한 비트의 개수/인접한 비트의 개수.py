#인접한 비트의 개수
x = 100
dp = [[[0]*2 for _ in range(x+1)] for _ in range(x+1)]
dp[1][0] = [1]*2

for i in range(2,x+1):
    for j in range(i+1):
        dp[i][j][0] = dp[i-1][j][1] + dp[i-1][j][0]
        dp[i][j][1] = dp[i-1][j-1][1] + dp[i-1][j][0]

t = int(input())
for case in range(t):
    n,k = map(int,input().split())
    print(sum(dp[n][k]))