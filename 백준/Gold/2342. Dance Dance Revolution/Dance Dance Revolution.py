def cal(a,b):
    if a == 0:
        return 2
    
    if a == b:
        return 1
    
    if (a+2)%4 == b%4:
        return 4
    
    return 3

max_ = int(1e9)

lst = list(map(int,input().split()))
n = len(lst)-1

dp = [[[max_]*5 for _ in range(5)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    tar = lst[i]
    for j in range(5):
        for k in range(5):
            if dp[i][j][k] == max_: continue

            if tar != k:
                cost = cal(j,tar)
                dp[i+1][tar][k] = min(dp[i+1][tar][k], dp[i][j][k] + cost)

            if tar != j:
                cost = cal(k,tar)
                dp[i+1][j][tar] = min(dp[i+1][j][tar], dp[i][j][k] + cost)

res = max_
for j in range(5):
    for k in range(5):
        res = min(res,dp[-1][j][k])

print(res)