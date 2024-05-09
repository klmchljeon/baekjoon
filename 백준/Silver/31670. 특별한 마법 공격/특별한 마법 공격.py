n = int(input())
d = [0] + list(map(int,input().split()))

dp = [0]*(n+1)
dp[1] = d[1]
for i in range(2,n+1):
    dp[i] = min(dp[i-1], dp[i-2]) + d[i]

print(min(dp[n],dp[n-1]))