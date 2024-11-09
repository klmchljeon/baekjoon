import sys
input = sys.stdin.readline
mod = int(1e9)+7

t = int(input())
for case in range(t):
    n,m,x,y,z = map(int,input().split())
    a = [int(input()) for _ in range(m)]

    lst = []
    for i in range(n):
        lst.append(a[i%m])
        a[i%m] = (x*a[i%m] + y*(i+1))%z

    dp = [0]*n
    for i in range(n):
        cnt = 1
        for j in range(i):
            if lst[i] > lst[j]:
                cnt += dp[j]

        dp[i] = cnt%mod

    res = sum(dp)%mod
    print(f'Case #{case+1}: {res}')