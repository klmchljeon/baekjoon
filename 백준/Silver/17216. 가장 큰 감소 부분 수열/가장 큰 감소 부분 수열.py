#가장 큰 감소 부분 수열
n = int(input())
d = [0]+list(map(int,input().split()))

dp = [0]*(n+1)

for i in range(n+1):
    dp[i] = d[i]
    for j in range(1,i):
        if d[j]>d[i]:
            dp[i] = max(dp[j]+d[i], dp[i])

print(max(dp))