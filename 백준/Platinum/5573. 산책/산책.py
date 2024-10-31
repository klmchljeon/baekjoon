dx = (1,0)
dy = (0,1)

h,w,n = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(h)]

dp = [[0]*w for _ in range(h)]
dp[0][0] = n-1

for x in range(h):
    for y in range(w):
        fir = dp[x][y]//2 + dp[x][y]%2
        sec = dp[x][y]//2
        p = [fir,sec][::(-1 if lst[x][y] else 1)]

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (nx<h and ny<w): continue

            dp[nx][ny] += p[i]

        lst[x][y] ^= dp[x][y]%2

x,y = 0,0
while x<h and y<w:
    idx = lst[x][y]
    x += dx[idx]
    y += dy[idx]

print(x+1,y+1)