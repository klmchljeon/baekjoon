t = int(input())
for case in range(t):
    n,d = map(int,input().split())
    st = input()

    dp = [-1]*n
    dp[0] = 0
    for i in range(n):
        if dp[i] == -1: continue

        for j in range(i+1,min(n,i+d+2)):
            if st[j] == 'X': continue

            if dp[j] == -1 or dp[j] > dp[i] + 1:
                dp[j] = dp[i] + 1

    print(f'Day #{case+1}')
    print(n,d)
    print(st)
    print(dp[-1] if dp[-1]!=-1 else 0)
    print()