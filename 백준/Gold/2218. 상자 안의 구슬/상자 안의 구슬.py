min_ = -int(1e9)

n,a,b = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
p = [0] + [i-1 for i in map(int,input().split())]
q = [0] + [i-1 for i in map(int,input().split())]

dp = [[min_]*(b+1) for _ in range(a+1)]
prev = [[None]*(b+1) for _ in range(a+1)]
dp[0][0] = 0
for i in range(1,a+1):
    dp[i][0] = 0
    prev[i][0] = (i-1,0,1)

for j in range(1,b+1):
    dp[0][j] = 0
    prev[0][j] = (0,j-1,2)

for x in range(1,a+1):
    for y in range(1,b+1):
        if x > 0 and dp[x][y] < dp[x-1][y]:
            dp[x][y] = dp[x-1][y]
            prev[x][y] = (x-1,y,1)

        if y > 0 and dp[x][y] < dp[x][y-1]:
            dp[x][y] = dp[x][y-1]
            prev[x][y] = (x,y-1,2)

        if x > 0 and y > 0 \
            and dp[x][y] < dp[x-1][y-1] + lst[p[x]][q[y]]:
            dp[x][y] = dp[x-1][y-1] + lst[p[x]][q[y]]
            prev[x][y] = (x-1,y-1,3)

res = []
loc = (x,y)
while True:
    x,y = loc
    if prev[x][y] != None:
        nx,ny,p = prev[x][y]
        res.append(p)
        loc = (nx,ny)
    else:
        break

print(dp[a][b])
print(*res[::-1])