dx = (1,0)
dy = (0,1)

n,m,k = map(int,input().split())
d = [list(input()) for _ in range(n)]

dp = [[False]*m for _ in range(n)]
for x in range(n-1,-1,-1):
    for y in range(m-1,-1,-1):
        if d[x][y] == '#': continue

        tmp = True
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (nx<n and ny<m): continue
            if d[nx][ny] == '#': continue
            tmp &= dp[nx][ny]

        for i in range(1,k+1):
            nx = x + i
            ny = y + i

            if not (nx<n and ny<m): continue
            if d[nx][ny] == '#': continue
            tmp &= dp[nx][ny]

        dp[x][y] = not tmp

q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    if dp[x-1][y-1]:
        print('First')
    else:
        print('Second')