inf = -int(1e9)

def dfs(x,y,z):
    if dp[x][y][z] != inf:
        return dp[x][y][z]
    
    tmp = inf
    if y<=x-1 and z<=x-1:
        tmp = max(tmp,dfs(x-1,y,z))

    if y<=x-1 and 0<=z-1:
        tmp = max(tmp,dfs(x-1,y,z-1))

    if 0<=y-1 and z<=x-1:
        tmp = max(tmp,dfs(x-1,y-1,z))

    if 0<=y-1 and 0<=z-1:
        tmp = max(tmp,dfs(x-1,y-1,z-1) + a[y-1]*b[z-1])

    dp[x][y][z] = tmp
    return dp[x][y][z]

n = int(input())
a = [i for i in map(int,input().split()) if i]
b = [i for i in map(int,input().split()) if i]
m,k = len(a),len(b)

dp = [[[inf]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
dp[0][0][0] = 0

print(dfs(n,m,k))