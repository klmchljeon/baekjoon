#엔비스카의 영혼
m = 10000000

n,a,b = map(int,input().split())
dp = [m]*(n+1)
if not n: 
    print(0)
    exit()

dp[0] = 0

for i in range(n+1):
    if dp[i] != m:
        if i+1 <= n:
            dp[i+1] = min(dp[i+1], dp[i] + 1)

        if i+1+a <= n:
            dp[i+1+a] = min(dp[i+1+a], dp[i] + 1)

        if i+1+b <= n:
            dp[i+1+b] = min(dp[i+1+b], dp[i] + 1)

print(dp[n])