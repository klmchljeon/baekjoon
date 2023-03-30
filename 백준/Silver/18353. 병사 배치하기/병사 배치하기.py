#병사 배치하기
n = int(input())
d = list(map(int,input().split()))
dp = [0]*n

for i in range(n):
    tmp = 1
    for j in range(i):
        if d[j] > d[i]:
            tmp = max(tmp,dp[j]+1)

    dp[i] = tmp

print(n-max(dp))