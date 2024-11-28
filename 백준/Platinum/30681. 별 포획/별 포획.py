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
if m == 2:
    print(dist(hull[0],hull[1])**0.5)
    exit()

res = None
e = 1
cur = dist(hull[0],hull[1])**0.5
for s in range(m):
    while ccw2(hull[(s-1)%m],hull[s],hull[e],hull[(e+1)%m]) >= 0:
        cur += dist(hull[e],hull[(e+1)%m])**0.5
        e = (e+1)%m

    if res == None or res > cur:
        res = cur

    cur -= dist(hull[s],hull[(s+1)%m])**0.5

print(res)