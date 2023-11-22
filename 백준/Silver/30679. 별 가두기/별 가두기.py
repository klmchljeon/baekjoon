#별 가두기
dx = (0,1,0,-1)
dy = (1,0,-1,0)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

res = []
for i in range(n):
    visit = [[[False]*4 for _ in range(m)] for _ in range(n)]
    di = 0
    x,y = (i,0)
    for k in range(4*n*m):
        nx = x + dx[di]*d[x][y]
        ny = y + dy[di]*d[x][y]
        if 0<=nx<n and 0<=ny<m:
            if not visit[nx][ny][di]:
                visit[nx][ny][di] = True
                x,y = nx,ny
                di = (di+1)%4
                continue

            else:
                res.append(i+1)
                break

        else:
            break

print(len(res))
if res:
    print(*res)