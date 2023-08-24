#진우의 달 여행 (Small)
dy = (-1,0,1)

max_ = int(1e9)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

dp = [[[max_]*3 for _ in range(m)] for _ in range(n)]
for j in range(m):
    for k in range(3):
        dp[0][j][k] = d[0][j]

for x in range(n-1):
    for y in range(m):
        for i in range(3):
            ny = y + dy[i]
            if not (0<=ny<m): continue

            for j in range(3):
                if i==j: continue
                dp[x+1][ny][j] = min(dp[x+1][ny][j], dp[x][y][i] + d[x+1][ny])

res = max_
for i in dp[-1]:
    res = min(res,min(i))

print(res)