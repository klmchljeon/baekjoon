#1로 만들기 2
n = int(input())
dp = [[n+1,0] for _ in range(n+1)]

dp[1][0] = 0

for i in range(1,n):
    if dp[i+1][0] > dp[i][0]:
        dp[i+1] = [dp[i][0]+1, i]

    if i*2<=n and dp[i*2][0] > dp[i][0]:
        dp[i*2] = [dp[i][0]+1, i]

    if i*3<=n and dp[i*3][0] > dp[i][0]:
        dp[i*3] = [dp[i][0]+1, i]

res = [n]
tmp = n
while tmp!=1:
    tmp = dp[tmp][1]
    res.append(tmp)

print(dp[n][0])
print(*res)