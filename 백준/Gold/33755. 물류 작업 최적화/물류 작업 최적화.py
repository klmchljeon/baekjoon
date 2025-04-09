#물류 작업 최적화
n = int(input())
lst = list(map(int,input().split()))

dp = [0]*(n+1)
for i in range(n):
    dp[i+1] = max(0,dp[i]) + lst[i]

p = dp[-1]

res = [0]*n
for i in range(n)[::-1]:
    if dp[i+1] >= 0:
        p = max(p,dp[i+1])
    else:
        p = max(0,p) + dp[i+1]

    res[i] = p

print(*res)