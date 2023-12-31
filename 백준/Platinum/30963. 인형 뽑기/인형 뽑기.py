import sys
input = sys.stdin.readline
mod = 1000000007

t = int(input())
for case in range(t):
    p,c,n = map(int,input().split())
    if c == 1:
        print(*range(1,n+1),sep='\n')
        continue

    if c > n:
        dp = [0]*(n+1)
        for k in range(1,n+1):
            dp[k] = (dp[k-1]*(1-p) + (dp[k-1]+1)*p)%mod

        print(*dp[1:],sep='\n')
        continue
    
    dp = [0]*(n+1)
    for k in range(1,c):
        dp[k] = (dp[k-1]*(1-p) + (dp[k-1]+1)*p)%mod

    p1_p = [1]*(c+1)

    tmp = 0
    for i in range(1,c+1):
        tmp = (tmp + (dp[c-i]+1)*p1_p[i-1]*p)%mod
        p1_p[i] = (p1_p[i-1]*(1-p))%mod

    for k in range(c,n+1):
        dp[k] = ((dp[k-c]+1)*p1_p[c] + tmp)%mod
        tmp = ((tmp - (dp[k-c]+1)*p1_p[c-1]*p)*(1-p) + (dp[k]+1)*p)%mod

    print(*dp[1:],sep='\n')