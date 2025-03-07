def check(num):
    max_ = 0
    p = num
    idx = 0
    for _ in range(m):
        while idx < n and lst[idx] <= p:
            max_ = lst[idx]
            idx += 1

        p += max_

    return p - num >= a

n,m,a = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

s,e = 0,int(1e5)
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

print(e)