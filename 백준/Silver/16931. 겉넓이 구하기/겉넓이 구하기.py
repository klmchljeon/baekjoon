dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
for x in range(n):
    for y in range(m):
        cnt += 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                cnt += max(0,lst[x][y]-lst[nx][ny])
            else:
                cnt += lst[x][y]

print(cnt)