#타일 채우기
n = int(input())
if n&1: 
    print(0)
    exit()

n //= 2

dp = [2]*(n+1)
dp[1] = 3
for i in range(2,n+1):
    dp[i] += dp[i-1]*3
    for j in range(2,i):
        dp[i] += dp[i-j]*2

print(dp[-1])