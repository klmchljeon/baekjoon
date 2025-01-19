import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

dic = dict(zip("UDLR",range(4)))
dx = (-1,1,0,0)
dy = (0,0,-1,1)

def dfs(loc):
    x,y = loc
    i = dic[lst[x][y]]
    nx = x + dx[i]
    ny = y + dy[i]
    
    if visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y]
        visited[nx][ny] = dfs((nx,ny))

    return visited[nx][ny]

n,m = map(int,input().split())
lst = [list(input().rstrip()) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            visited[i][j] = cnt
            visited[i][j] = dfs((i,j))
            if visited[i][j] == cnt:
                cnt += 1

print(cnt)