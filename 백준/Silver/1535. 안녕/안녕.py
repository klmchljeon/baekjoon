n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[-1]*(101) for _ in range(n+1)]
dp[0][100] = 0
for i in range(n):
    for j in range(1,101):
        if dp[i][j] != -1:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j-a[i] > 0:
                dp[i+1][j-a[i]] = max(dp[i+1][j-a[i]], dp[i][j] + b[i])

print(max(dp[n]))