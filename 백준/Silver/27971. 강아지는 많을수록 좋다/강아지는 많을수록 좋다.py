max_ = int(1e9)
n,m,a,b = map(int,input().split())

danger = [0]*(n+1)
for _ in range(m):
    l,r = map(int,input().split())
    for i in range(l,r+1):
        danger[i] = 1

dp = [max_]*(n+1)
dp[0] = 0

for i in range(1,n+1):
    if danger[i]: continue

    if i >= a:
        dp[i] = min(dp[i], dp[i-a]+1)

    if i >= b:
        dp[i] = min(dp[i], dp[i-b]+1)

print(dp[n] if dp[n]!=max_ else -1)