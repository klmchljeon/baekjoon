import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
if n == 1:
    print(lst[0])
    exit()

dp = [[0,0] for _ in range(n)]
dp[0] = [lst[0]]*2
dp[1] = [dp[0][0]+lst[1]//2, lst[1]]
for i in range(2,n):
    dp[i][0] = dp[i-1][1] + lst[i]//2
    dp[i][1] = max(*dp[i-2],*dp[i-3]) + lst[i]
    
res = 0
for i in range(n):
    res = max(res,max(dp[i]))

print(res)