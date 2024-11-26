import sys
from math import ceil
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

case = 0
while True:
    n = int(input())
    if not n: break

    d = []
    for _ in range(n):
        x,y = map(int,input().split())
        d.append((x,y))

    d.sort()

    hull = []
    hull += convex(d)
    hull += convex(d[::-1])

    m = len(hull)
    
    res = int(1e9)
    for s in range(m):
        e = (s+2)%m
        tmp = 0
        for _ in range(m):
            x1,y1 = hull[s]
            x2,y2 = hull[(s+1)%m]
            x3,y3 = hull[e]

            a,b = y2-y1,x1-x2
            c = -a*x1 - b*y1

            d = abs(a*x3 + b*y3 + c) / (a**2 + b**2)**0.5
            tmp = max(tmp,d)

            e = (e+1)%m

        res = min(res,tmp)

    print(f'Case {case+1}: {ceil(res*100)/100:.2f}')
    case += 1