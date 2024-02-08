def check(num):
    cnt = 0
    for i in d:
        if i > num:
            cnt += i-num

    return cnt <= k

n,k = map(int,input().split())
d = list(map(int,input().split()))

s,e = -1,int(1e18)
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid
    else:
        s = mid

print(e)