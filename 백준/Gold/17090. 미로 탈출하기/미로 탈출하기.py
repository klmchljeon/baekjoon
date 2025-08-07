#미로 탈출하기
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(loc,visit):
    visit.add(loc)
    x,y = loc
    if dp[x][y] != None:
        return dp[x][y]

    i = dic[d[x][y]]
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<m:
        if (nx,ny) in visit:
            return False

        dp[x][y] = dfs((nx,ny),visit)
        return dp[x][y]

    dp[x][y] = True
    return True

dic = {'U':0,'D':1,'L':2,'R':3}
dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [input().rstrip() for _ in range(n)]

dp = [[None]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if dp[i][j] == None:
            dfs((i,j),set())

cnt = 0
for i in dp:
    cnt += i.count(True)

print(cnt)