#점프 점프
max_ = 10000

n = int(input())
d = list(map(int,input().split()))

dp = [max_]*n
dp[0] = 0
for i in range(n):
    for j in range(1,d[i]+1):
        if i+j >= n: break
        dp[i+j] = min(dp[i+j], dp[i]+1)

res = dp[-1] if dp[-1]!=max_ else -1
print(res)