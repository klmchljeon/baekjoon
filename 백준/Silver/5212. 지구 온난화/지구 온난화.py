dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [input() for _ in range(n)]

res = [['.']*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if d[x][y] == '.': 
            continue

        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue

            if d[nx][ny] == 'X':
                cnt += 1

        if cnt >= 2:
            res[x][y] = 'X'

min_ = [n,m]
max_ = [0,0]
for i in range(n):
    for j in range(m):
        if res[i][j] == 'X':
            min_[0] = min(min_[0],i)
            min_[1] = min(min_[1],j)
            max_[0] = max(max_[0],i)
            max_[1] = max(max_[1],j)

for i in range(min_[0],max_[0]+1):
    for j in range(min_[1],max_[1]+1):
        print(res[i][j], end = '')
    print()