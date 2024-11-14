t = int(input())
for case in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    m = int(input())
    dp = [[0]*n for _ in range(m+1)]
    for i in range(n):
        if lst[i] <= m:
            dp[lst[i]][i] = 1

    for i in range(1,m+1):
        for j in range(n):
            for k in range(j+1):
                if i+lst[j] <= m:
                    dp[i+lst[j]][j] += dp[i][k]

    print(sum(dp[m]))