n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [[-1]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(n+1):
        if dp[i][j] == -1: continue

        if i<n and j<n:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
        
        if i<n:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        if i<n and j<n and a[i]>b[j]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j]+b[j])

p = 0
for i in dp:
    p = max(p,max(i))

print(p)