import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    a,b,c = map(int,input().split())
    lst.append(c)

dp = [[0]*2 for _ in range(n+1)]
dp[1][1] = lst[0]
for i in range(2,n+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + lst[i-1]

print(max(dp[n]))