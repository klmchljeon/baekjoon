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

def ccw2(a,b,c,d):
    d = (d[0]-c[0]+b[0],d[1]-c[1]+b[1])
    return ccw(a,b,d)

def calipers(hull):
    m = len(hull)
    if m == 2:
        return dist(hull[0],hull[1])

    res = 0
    e = 1
    for s in range(m):
        cur = dist(hull[s],hull[e])
        while ccw2(hull[s],hull[(s+1)%m],hull[e],hull[(e+1)%m]) > 0:
            e = (e+1)%m

            cur = dist(hull[s],hull[e])

            if res < cur:
                res = cur

    return res

def gen(lst,t):
    tmp = []
    for x,y,dx,dy in lst:
        tmp.append((x+dx*t,y+dy*t))

    if len(tmp) < 3:
        return tmp

    tmp.sort()

    res = []
    res += convex(tmp)
    res += convex(tmp[::-1])

    return res

def check(num):
    a = calipers(gen(d,num))
    b = calipers(gen(d,num+1))

    return a <= b

n,t = map(int,input().split())
d = []
for _ in range(n):
    x,y,dx,dy = map(int,input().split())
    d.append((x,y,dx,dy))

s,e = -1,t
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

print(e)
print(calipers(gen(d,e)))