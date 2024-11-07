n = int(input())
dp = [n]*(n+1)
for i in range(n+1):
    dp[i] = min(dp[i],i)
    for p in (2,5,7):
        if i+p < n+1:
            dp[i+p] = min(dp[i+p], dp[i]+1)

print(dp[n])