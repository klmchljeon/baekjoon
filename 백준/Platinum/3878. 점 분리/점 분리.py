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
        if tmp == 0:
            if intersect((lst[i],lst[(i+1)%n]),(p,p)):
                continue
            else:
                return False

        if cur != None and tmp * cur < 0:
            return False

        cur = tmp

    return True

def check(lst1,lst2):
    if len(lst2) == 0: return True
    if len(lst1) == 1: return True
    
    if len(lst1) == 2:
        if len(lst2) == 1:
            return not intersect(lst1,lst2+lst2)
        else:
            return not intersect(lst1,lst2)
        
    for i in lst2:
        if inside(lst1,i):
            return False
        
    if len(lst2) >= 3:
        for i in lst1:
            if inside(lst2,i):
                return False
    
    n,m = len(lst1),len(lst2)
    for i in range(n):
        for j in range(m):
            if intersect((lst1[i],lst1[(i+1)%n]),(lst2[j],lst2[(j+1)%m])):
                return False
        
    return True

t = int(input())
for case in range(t):
    n,m = map(int,input().split())
    d = []
    for _ in range(n):
        x,y = map(int,input().split())
        d.append((x,y))

    d.sort()

    hull1 = []
    if n >= 3:
        hull1 += convex(d)
        hull1 += convex(d[::-1])
    else:
        hull1 = d[:]

    d = []
    for _ in range(m):
        x,y = map(int,input().split())
        d.append((x,y))

    d.sort()

    hull2 = []
    if m >= 3:
        hull2 += convex(d)
        hull2 += convex(d[::-1])
    else:
        hull2 = d[:]

    if len(hull1) < len(hull2):
        hull1,hull2 = hull2,hull1

    print('YES' if check(hull1,hull2) else 'NO')