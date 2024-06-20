n,k = map(int,input().split())

s,e = -1,n//2
while s+1<e:
    mid = (s+e)//2

    if (mid+1)*(n-mid+1) >= k:
        e = mid

    else:
        s = mid

if (e+1)*(n-e+1) == k:
    print('YES')
else:
    print('NO')