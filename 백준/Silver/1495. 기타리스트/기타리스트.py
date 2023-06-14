#기타리스트
n,s,m = map(int,input().split())
d = [0] + list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1,n+1):
    for j in range(m+1):
        if not dp[i-1][j]: continue

        up = j+d[i]
        if up <= m:
            dp[i][up] = 1

        down = j-d[i]
        if down >= 0:
            dp[i][down] = 1

for j in range(m,-1,-1):
    if dp[n][j]:
        print(j)
        break

else:
    print(-1)