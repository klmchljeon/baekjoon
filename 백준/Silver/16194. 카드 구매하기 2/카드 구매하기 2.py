#카드 구매하기 2
max_ = int(1e9)

n = int(input())
d = [0] + list(map(int,input().split()))

dp = d[:]
for i in range(1,n+1):
    tmp = max_
    for j in range(i):
        tmp = min(tmp,dp[i-j]+d[j])

    dp[i] = tmp

print(dp[n])