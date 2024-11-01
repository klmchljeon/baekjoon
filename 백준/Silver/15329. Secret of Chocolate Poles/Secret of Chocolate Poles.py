l,k = map(int,input().split())
dp = [0]*l
dp[0] = 1
if k-1 < l:
    dp[k-1] = 1

for i in range(l):
    if dp[i]:
        if i+1+1 < l:
            dp[i+1+1] += dp[i]

        if i+k+1 < l:
            dp[i+k+1] += dp[i]

print(sum(dp))