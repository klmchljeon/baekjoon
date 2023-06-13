#상자넣기
n = int(input())
d = list(map(int,input().split()))

dp = [0]*n

for i in range(n):
    tmp = 0
    for j in range(i):
        if d[i] > d[j]:
            tmp = max(tmp,dp[j])

    dp[i] = tmp + 1

print(max(dp))