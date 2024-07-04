def check(num):
    cnt = 1
    prev = lst[0]
    for i in range(1,n):
        if lst[i] - prev >= num:
            cnt += 1
            prev = lst[i]

    return cnt >= s

t = int(input())
for case in range(t):
    n,s = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()

    lo,hi = 0,int(1e9)
    while lo+1<hi:
        mid = (lo+hi)//2

        if check(mid):
            lo = mid

        else:
            hi = mid

    print(lo)