#떡장수와 호랑이
n = int(input())

dp = [[0]*10 for _ in range(n)]
_,*fir = map(int,input().split())
for j in fir:
    dp[0][j] = 1

for i in range(1,n):
    _,*tmp = map(int,input().split())

    cnt = 2
    for j in range(1,10):
        if not dp[i-1][j]: continue
        cnt -= 1

        for k in tmp:
            if j != k:
                dp[i][k] = j

        if not cnt:
            break

res = []
for j in range(1,10):
    if dp[n-1][j]:
        res.append(j)
        break

if not res:
    print(-1)
    exit()

for i in range(n-1,0,-1):
    res.append(dp[i][res[-1]])

print(*res[::-1],sep='\n')