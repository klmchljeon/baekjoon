n = int(input())
lst = [int(input()) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
for s in range(n):
    dp[s][s] = lst[s]

for gap in range(n-1):
    for i in range(n):
        s,e = i,(i+gap)%n
        if dp[s][e] == 0: continue

        if gap%2 == 0:
            if lst[(s-1)%n] > lst[(e+1)%n]:
                dp[(s-1)%n][e] = max(dp[(s-1)%n][e], dp[s][e])

            else:
                dp[s][(e+1)%n] = max(dp[s][(e+1)%n], dp[s][e])

        else:
            dp[(s-1)%n][e] = max(dp[(s-1)%n][e], dp[s][e] + lst[(s-1)%n])
            dp[s][(e+1)%n] = max(dp[s][(e+1)%n], dp[s][e] + lst[(e+1)%n])

res = 0
for i in range(n):
    res = max(res,dp[i][(i-1)%n])

print(res)