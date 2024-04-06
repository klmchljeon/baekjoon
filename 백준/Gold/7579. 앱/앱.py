max_ = 10000

n,m = map(int,input().split())
v = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))

dp = [[0]*(max_+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(max_+1):
        if c[i] > j:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]] + v[i])

for j in range(max_+1):
    if dp[n][j] >= m:
        print(j)
        break