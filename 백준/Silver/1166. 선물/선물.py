def check(a):
    p = 1                                                                                                                                                                          
    for i in (l,w,h):
        p *= i//a

    return p >= n

n,l,w,h = map(int,input().split())
s,e = 0,int(1e9)+1

for _ in range(100):
    mid = (s+e)/2

    if check(mid):
        s = mid
    else:
        e = mid

print(s)