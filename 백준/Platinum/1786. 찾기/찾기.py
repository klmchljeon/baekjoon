#찾기 
def pre():
    dp = [0]*m

    cur = 0
    for i in range(1,m):
        while cur and p[i] != p[cur]:
            cur = dp[cur-1]

        if p[i] == p[cur]:
            cur += 1
            dp[i] = cur

    return dp

t = input(); n = len(t)
p = input(); m = len(p)
pi = pre()

res = []

cur = 0
for i in range(n):
    while cur and t[i] != p[cur]:
        cur = pi[cur-1]

    if t[i] == p[cur]:
        if cur==m-1:
            res.append(i-m+2)
            cur = pi[cur]

        else:
            cur += 1

print(len(res))
if res:
    print(*res)