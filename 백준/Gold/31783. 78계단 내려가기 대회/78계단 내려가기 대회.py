def find(idx,wei):
    s,e = -1,idx
    while s+1<e:
        mid = (s+e)//2

        if lst[mid] - lst[idx] >= wei:
            s = mid

        else:
            e = mid

    return s

n = int(input())
lst = list(map(int,input().split()))
a = [0] + list(map(int,input().split()))
b = [0] + list(map(int,input().split()))

dp = [0]*n
for i in range(1,n):
    dp[i] = dp[i-1]
    
    p = find(i,b[i])
    if p != -1:
        dp[i] = max(dp[i], dp[p]+a[i])

print(dp[n-1])