inf = int(1e9)

n,m = map(int,input().split())
lst = []
for _ in range(m):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

dp = [[0]*m for _ in range(n+1)]
for i in range(1,n+1):
    tmp = [(-inf,-1),(-inf,-1)]
    for j in range(m):
        if tmp[0][0] < dp[i-1][j]:
            tmp[1] = tmp[0]
            tmp[0] = (dp[i-1][j],j)

        elif tmp[1][0] < dp[i-1][j]:
            tmp[1] = (dp[i-1][j],j)

    for j in range(m):
        if tmp[0][1] != j or i == 1:
            dp[i][j] = tmp[0][0] + lst[j][i-1]

        else:
            dp[i][j] = max(tmp[0][0] + lst[j][i-1]//2,
                           tmp[1][0] + lst[j][i-1])
    
print(max(dp[n]))