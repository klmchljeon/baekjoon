#볼록 껍질
import sys
input = sys.stdin.readline

ccw = lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])
def convex(lst):
    res = []
    for i in lst:
        while len(res) >= 2 and ccw(*res[-2:],i) <= 0:
            res.pop()
        res.append(i)

    res.pop()
    return res

n,m = map(int,input().split())
lst1 = []
for _ in range(n):
    x,y = map(int,input().split())
    lst1.append((x,y))

lst2 = []
for _ in range(m):
    x,y = map(int,input().split())
    lst2.append((x,y))

d = []
for x1,y1 in lst1:
    for x2,y2 in lst2:
        d.append((x1+x2,y1+y2))

d.sort()

hull = []
hull += convex(d)
hull += convex(d[::-1])

p = hull[0]
idx = 0
for i in range(len(hull)):
    if p > hull[i]:
        p = hull[i]
        idx = i

m = len(hull)
print(m)
for i in range(m):
    print(*hull[(idx+i)%m])