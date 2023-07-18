#색종이 만들기
def dfs(x,y,n,c):
    global count
    if n == 1: 
        if d[x][y] == c:
            count[c] += 1
        return 

    for i in range(x,x+n):
        for j in range(y,y+n):
            if d[i][j] != c:
                for k in range(4):
                    nx = x + dx[k]*n//2
                    ny = y + dy[k]*n//2
                    dfs(nx,ny,n//2,c)
                return 

    count[c] += 1
    return

dx = (0,0,1,1)
dy = (0,1,0,1)

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
count = [0,0]
dfs(0,0,n,1)
dfs(0,0,n,0)
print(*count,sep='\n')