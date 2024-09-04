n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        tmp = 0
        for px,py in ((x-1,y),(x,y-1)):
            if not (0<=px<n and 0<=py<n):
                continue

            tmp = max(tmp, dp[px][py])

        dp[x][y] = tmp + lst[x][y]*(1<<(2*n-x-y-2))

print(dp[n-1][n-1])