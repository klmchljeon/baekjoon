dp = [0,1,1,1]
n = int(input())
for i in range(4,n+1):
    dp.append(dp[i-1] + dp[i-3])

print(dp[n])