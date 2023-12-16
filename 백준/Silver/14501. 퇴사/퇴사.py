#퇴사 
n = int(input())
d = [None]*(n+1)
for i in range(n,0,-1):
    d[i] = tuple(map(int,input().split()))

dp = [0]*(n+1)
for i in range(1,n+1):
    if d[i][0] > i:
        dp[i] = dp[i-1]
    else:
        dp[i] = max(dp[i-1],dp[i-d[i][0]]+d[i][1])

print(dp[n])