m = 30
dp = [1]*2 + [0]*(m-1)
for i in range(2,m+1):
    dp[i] += dp[i-1]
    dp[i] += 2*dp[i-2]

n = int(input())

if n&1:
    p = dp[n//2]
else:
    p = 2*dp[n//2-1] + dp[n//2]

print(dp[n] - (dp[n]-p)//2)