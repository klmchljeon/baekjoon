n = int(input())

lst = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        tmp = 0
        for px in range(x+1):
            for py in range(y+1):
                if lst[px][py] < lst[x][y]:
                    tmp = max(tmp, dp[px][py])

        dp[x][y] = tmp+1

res = 0
for i in dp:
    res = max(res,max(i))

print(res)