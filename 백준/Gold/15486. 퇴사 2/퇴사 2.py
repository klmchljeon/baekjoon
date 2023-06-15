#퇴사 2
import sys
input = sys.stdin.readline

n = int(input())
d = []
for _ in range(n):
    t,p = map(int,input().split())
    d.append((t,p))

dp = [0]*(n+1)
for i in range(n):
    t = i + d[i][0] - 1
    if t < n:
        cost = dp[i] + d[i][1]
        dp[t+1] = max(dp[t+1],cost)
    
    dp[i+1] = max(dp[i+1],dp[i])

print(dp[-1])