#볼록 껍질
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

    return dist(hull[i],hull[(i+s)%m])

def check(i,mid):
    a = dist(hull[i],hull[(i+mid)%m])
    b = dist(hull[i],hull[(i+mid-1)%m])
    return a - b > 0

n = int(input())
d = []
for _ in range(n):
    x,y = map(int,input().split())
    d.append((x,y))

d.sort()

hull = []
hull += convex(d)
hull += convex(d[::-1])

hull = hull[::-1]
m = len(hull)
res = 0
for i in range(m):
    res = max(res,find(i))

print(res)