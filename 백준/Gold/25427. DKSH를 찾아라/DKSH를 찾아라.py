dic = dict(zip('DKSH',range(1,5)))

n = int(input())
st = [''] + list(input())

dp = [[1] + [0]*4 for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,5):
        dp[i][j] = dp[i-1][j]

    if st[i] in dic:
        dp[i][dic[st[i]]] += dp[i][dic[st[i]]-1]

print(dp[n][4])