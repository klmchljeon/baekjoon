#빵집 30:53
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfs(x,y=0):
    global suc
    if y == c-1:
        suc = True
        return 1
    
    tmp = 0
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if suc or not (0<=nx<r): continue

        if not visit[nx][ny] and d[nx][ny] == '.':
            visit[nx][ny] = True
            tmp = dfs(nx,ny)

    return tmp

dx = (-1,0,1)

r,c = map(int,input().split())
d = [list(input()) for _ in range(r)]

visit = [[False]*c for _ in range(r)]

cnt = 0
for i in range(r):
    suc = False
    visit[i][0] = True
    cnt += dfs(i)

print(cnt)