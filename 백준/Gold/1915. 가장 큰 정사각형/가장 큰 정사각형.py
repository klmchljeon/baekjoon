#가장 큰 정사각형 13:46
dx = (-1,0,-1)
dy = (0,-1,-1)

n,m = map(int,input().split())
d = [list(map(int,input())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if not d[x][y]: continue

        dp[x][y] = 1
        if not (x and y): continue

        tmp = 1001
        for i in range(3):
            px = x + dx[i]
            py = y + dy[i]

            tmp = min(tmp,dp[px][py])

        dp[x][y] = tmp + 1

res = 0
for i in range(n):
    for j in range(m):
        res = max(res,dp[i][j])

print(res**2)