#동전 2
m = 100000

n,k = map(int,input().split())
d = [int(input()) for _ in range(n)]

d = sorted(set(d))
while d and d[-1] > k:
    d.pop()

dp = [m]*(k+1)
for i in d:
    dp[i] = 1

for i in range(1,k+1):
    for j in d:
        if i-j > 0 and dp[i-j] != m:
            dp[i] = min(dp[i], dp[i-j]+1)

print(dp[k] if dp[k]!=m else -1)