max_ = 40000

n = int(input())
d = list(map(int,input().split()))

m = int(input())
lst = list(map(int,input().split()))

dp = [[0]*(2*max_+1) for _ in range(n+1)]
dp[0][max_] = 1
for i in range(n):
    for w in range(2*max_+1):
        if dp[i][w] == 0:
            continue

        for k in (-1,0,1):
            nw = w + d[i]*k
            dp[i+1][nw] = 1

res = []
for i in lst:
    tmp = 'Y' if dp[n][i+max_] else 'N'
    res.append(tmp)

print(*res)