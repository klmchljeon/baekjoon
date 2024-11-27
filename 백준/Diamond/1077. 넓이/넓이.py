import sys
input = sys.stdin.readline

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def convex(lst):
    res = []
    for i in lst:
        while len(res) >= 2 and ccw(*res[-2:],i) <= 0:
            res.pop()
        res.append(i)

    res.pop()
    return res

def intersect(l1,l2):
    p1,p2 = l1
    p3,p4 = l2

    ccw1 = ccw(p1,p2,p3)*ccw(p1,p2,p4)
    ccw2 = ccw(p3,p4,p1)*ccw(p3,p4,p2)

    if ccw1==0 and ccw2==0:
        if p1>p2: p1,p2 = p2,p1
        if p3>p4: p3,p4 = p4,p3
        return p3<=p2 and p1<=p4

    return ccw1<=0 and ccw2<=0

def inside(lst,p):
    cur = None
    n = len(lst)
    for i in range(n):
        tmp = ccw(lst[i],lst[(i+1)%n],p)
        if cur != None and tmp * cur <= 0:
            return False

        cur = tmp

    return True

def gen(lst):
    if len(lst) < 3:
        return lst
    
    lst.sort()
    res = convex(lst) + convex(lst[::-1])
    return res

def cal(a,b):
    x = a[1]-b[1]
    y = -(a[0]-b[0])
    c = -a[0]*(b[1]-a[1]) + a[1]*(b[0]-a[0])
    return x,y,c

def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]

def mul(a,b,d):
    x = (a[0][0]*b[0] + a[0][1]*b[1])
    y = (a[1][0]*b[0] + a[1][1]*b[1])
    return x/d, y/d
    
def f(l1,l2):
    a,b = l1
    c,d = l2

    p = [[],[]]
    q = []

    x,y,z = cal(a,b)
    p[0] = [x,y]
    q.append(z)

    x,y,z = cal(c,d)
    p[1] = [x,y]
    q.append(z)

    inv = [[p[1][1],-p[0][1]],[-p[1][0],p[0][0]]]
    res = mul(inv,q,det(p))
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

tmp = []
for i in lst1:
    if inside(lst2,i):
        tmp.append(i)

for i in lst2:
    if inside(lst1,i):
        tmp.append(i)

for i in range(n):
    for j in range(m):
        l1 = (lst1[i],lst1[(i+1)%n])
        l2 = (lst2[j],lst2[(j+1)%m])
        if not intersect(l1,l2):
            continue

        tmp.append(f(l1,l2))

hull = gen(tmp)
p = len(hull)

res = 0
for i in range(p):
    res += hull[i][0]*hull[(i+1)%p][1] - hull[i][1]*hull[(i+1)%p][0]

print(res/2)