max_ = int(1e9)

n,c = map(int,input().split())
lst = []
for _ in range(c):
    a,b = map(int,input().split())
    lst.append((a,b))

dp = [max_]*(n+1)
dp[0] = 0

for i in range(n):
    for a,b in lst:
        idx = min(n,i+b)
        dp[idx] = min(dp[idx],dp[i]+a)

print(dp[n])