def check(p):
    s,e = 0,p
    for _ in range(100):
        mid = (e+s)/2

        ex = x*((p-mid)/p)
        hx = (ex**2 - (p-mid)**2)

        sy = y*(mid/p)
        hy = (sy**2 - mid**2)

        if hx >= hy:
            s = mid

        else:
            e = mid

    return hx**0.5 > c

x,y,c = map(float,input().split())
s,e = 0,min(x,y)
for _ in range(100):
    mid = (e+s)/2

    if check(mid):
        s = mid

    else:
        e = mid

print(s)