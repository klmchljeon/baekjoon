import sys
input = sys.stdin.readline

dist = lambda a,b:(a[0]-b[0])**2 + (a[1]-b[1])**2
ccw = lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])

def convex(lst):
    res = []
    for i in lst:
        while len(res) >= 2 and ccw(*res[-2:],i) <= 0:
            res.pop()
        res.append(i)

    res.pop()
    return res

def find(i):
    s,e = 0,n
    while s+1<e:
        mid = (s+e)//2
        
        if check(i,mid):
            s = mid

        else:
            e = mid

    return hull[i],hull[(i+s)%m]

def check(i,mid):
    a = dist(hull[i],hull[(i+mid)%m])
    b = dist(hull[i],hull[(i+mid-1)%m])
    return a - b > 0

def ccw2(a,b,c,d):
    d = (d[0]-c[0]+b[0],d[1]-c[1]+b[1])
    return ccw(a,b,d)

t = int(input())
for case in range(t):
    n = int(input())
    d = []
    for _ in range(n):
        x,y = map(int,input().split())
        d.append((x,y))

    d.sort()

    hull = []
    hull += convex(d)
    hull += convex(d[::-1])

    m = len(hull)
    
    res = (0,(0,1))
    e = 1
    for s in range(m):
        cur = dist(hull[s],hull[e])
        while ccw2(hull[s],hull[(s+1)%m],hull[e],hull[(e+1)%m]) > 0:
            e = (e+1)%m

            cur = dist(hull[s],hull[e])

            if res[0] < cur:
                res = (cur,(s,e))

    s,e = res[1]
    print(*hull[s],*hull[e])