#이동하기
dx = (1,0,1)
dy = (0,1,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0][0] = d[0][0]

for x in range(n):
    for y in range(m):
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (nx<n and ny<m): continue

            dp[nx][ny] = max(dp[nx][ny], d[nx][ny]+dp[x][y])

print(dp[n-1][m-1])