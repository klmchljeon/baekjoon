inf = int(1e9)

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if n > m:
    n,m = m,n
    a,b = b,a

a.sort()
b.sort()
    
dp = [[[0,inf] for _ in range(m+1)] for _ in range(n)]
k = inf
for j in range(1,m+1):
    dp[0][j][0] = abs(a[0]-b[j-1])
    k = min(k,dp[0][j][0])
    dp[0][j][1] = k

for i in range(1,n):
    for j in range(1,m+1):
        dp[i][j][0] = dp[i-1][j-1][1] + abs(a[i]-b[j-1])
        dp[i][j][1] = min(dp[i][j-1][1], dp[i][j][0])

print(dp[-1][-1][1])