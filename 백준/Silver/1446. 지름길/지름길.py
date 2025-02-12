max_ = 10001

n,d = map(int,input().split())
lst = []
for _ in range(n):
    a,b,c = map(int,input().split())
    lst.append((a,b,c))

lst.sort(reverse=True)

dp = [max_]*(d+1)
dp[0] = 0
for i in range(d):
    while lst and lst[-1][0] == i:
        a,b,c = lst.pop()
        if b > d: continue
        dp[b] = min(dp[b],dp[a]+c)

    dp[i+1] = min(dp[i+1],dp[i]+1)

print(dp[d])