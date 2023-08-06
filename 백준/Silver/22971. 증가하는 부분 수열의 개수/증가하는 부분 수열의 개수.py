mod = 998244353

n = int(input())
d = [0]+list(map(int,input().split()))
dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = 1
    for j in range(1,i):
        if d[j]<d[i]:
            dp[i] += dp[j]
            
    dp[i] %= mod

print(*dp[1:])