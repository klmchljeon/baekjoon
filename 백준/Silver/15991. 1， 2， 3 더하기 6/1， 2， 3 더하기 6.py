max_ = 100000
mod = int(1e9) + 9

dp = [[0]*4 for _ in range(max_+1)]
for i in (1,2,3):
    dp[i][i] = 1

for i in range(2,max_+1):
    for j in (1,2,3):
        dp[i][j] += sum(dp[i-j])%mod

t = int(input())
for case in range(t):
    n = int(input())
    
    res = 0
    if n%2 == 0:
        res += sum(dp[n//2])
        res += dp[(n-2)//2+2][2]

    else:
        res += dp[(n-1)//2+1][1]
        res += dp[(n-3)//2+3][3]

    print(res%mod)
