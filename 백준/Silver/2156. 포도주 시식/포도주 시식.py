#포도주 시식
n = int(input())
d = [0]+[int(input()) for _ in range(n)]
dp = [[0,0] for _ in range(n+1)]
dp[1] = [d[1],d[1]]
i2 = 0
i3 = 0
for i in range(2,n+1):
    dp[i][0] = d[i]+i2
    dp[i][1] = d[i]+d[i-1]+i3
    i2 = max([i2]+dp[i-1])
    i3 = max([i3]+dp[i-2])

result = max(dp[n-1]+dp[n])
print(result)