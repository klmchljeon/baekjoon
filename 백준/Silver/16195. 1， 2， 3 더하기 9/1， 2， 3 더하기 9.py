import sys
input = sys.stdin.readline
mod = int(1e9)+9
n,m = 1000,1000

dp = [[0]*(m+1) for _ in range(n+1)]
for i in (1,2,3):
    dp[i][1] = 1

dp[2][2] = 1

for i in range(3,n+1):
    for j in range(1,m+1):
        if j > i: break

        dp[i][j] = (dp[i][j] + dp[i-1][j-1])%mod
        dp[i][j] = (dp[i][j] + dp[i-2][j-1])%mod
        dp[i][j] = (dp[i][j] + dp[i-3][j-1])%mod

prefix = [[] for _ in range(n+1)]
for i in range(n+1):
    s = 0
    for j in range(m+1):
        s = (s + dp[i][j])%mod
        prefix[i].append(s)

t = int(input())
for case in range(t):
    i,j = map(int,input().split())
    print(prefix[i][j])