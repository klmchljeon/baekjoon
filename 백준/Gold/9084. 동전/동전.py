#동전 10:54
t = int(input())
for case in range(t):
    n = int(input())
    d = list(map(int,input().split()))
    m = int(input())

    d.sort()
    while d and d[-1] > m:
        d.pop()

    dp = [0]*(m+1)
    for i in d:
        dp[i] += 1
        for j in range(i+1,m+1):
            dp[j] += dp[j-i]

    print(dp[m])