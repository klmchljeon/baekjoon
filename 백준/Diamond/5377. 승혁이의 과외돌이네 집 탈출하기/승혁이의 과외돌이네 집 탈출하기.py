#볼록 껍질
import sys
input = sys.stdin.readline

ccw = lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])
dist = lambda a,b:(a[0]-b[0])**2+(a[1]-b[1])**2

def convex(lst):
    res = []
    for i in lst:
        while len(res) >= 2 and ccw(*res[-2:],i) <= 0:
            res.pop()
        res.append(i)

    res.pop()
    return res

def gen(lst):
    if len(lst) < 3:
        return lst
    
    res = convex(lst) + convex(lst[::-1])
    return res

def intersect(l1,l2):
    p1,p2 = l1
    p3,p4 = l2
    if inline(l1,p3) or inline(l1,p4): return False
    if inline(l2,p1) or inline(l2,p2): return False

    ccw1 = ccw(p1,p2,p3)*ccw(p1,p2,p4)
    ccw2 = ccw(p3,p4,p1)*ccw(p3,p4,p2)

    if ccw1==0 and ccw2==0:
        if p1>p2: p1,p2 = p2,p1
        if p3>p4: p3,p4 = p4,p3
        return p3<=p2 and p1<=p4

    return ccw1<=0 and ccw2<=0

def inline(line,p):
    x,y = line
    f1 = ccw(x,y,p)==0
    f2 = dist(x,y)**0.5 - (dist(x,p)**0.5 + dist(p,y)**0.5) < 1e-9
    return f1 and f2

def inside(lst,p):
    cur = None
    n = len(lst)
    for i in range(n):
        tmp = ccw(lst[i],lst[(i+1)%n],p)
        if tmp == 0: return 0,i

        if cur != None and tmp * cur < 0:
            return -1,None

        cur = tmp

    return 1,None

def check(lst1,lst2):
    if len(lst1) == 1: return False
    if len(lst1) == 2:
        return not intersect(lst1,lst2)

    for i in lst2:
        if inside(lst1,i)[0] == 1:
            return False

    n = len(lst1)
    for i in range(n-1):
        for j in range(i,n):
            if intersect((lst1[i],lst1[j]),lst2):
                #print(lst1[i],lst1[(i+1)%n],lst2)
                return False
        
    return True

def circ(lst):
    res = dist(lst[0],lst[-1])**0.5
    for i in range(len(lst)-1):
        res += dist(lst[i],lst[i+1])**0.5

    return res 

t = int(input())
for case in range(t):
    loc1 = tuple(map(int,input().split()))
    loc2 = tuple(map(int,input().split()))
    n = int(input())
    d = []
    for _ in range(n):
        x,y = map(int,input().split())
        d.append((x,y))

    d.sort()

    hull = gen(d)

    flag = False
    inside1,idx1 = inside(hull,loc1)
    inside2,idx2 = inside(hull,loc2)
    if inside1==0 and inside2==0:
        if idx1 != idx2:
            flag = True
        
    if inside1==0 or inside2==0:
        if inside1 != 0:
            inside1,inside2 = inside2,inside1
            idx1,idx2 = idx2,idx1
            loc1,loc2 = loc2,loc1

        p1,p2 = hull[idx1],hull[(idx1+1)%len(hull)]
        lst = [[],[]]
        for i in hull:
            c = ccw(p1,p2,i)
            if c > 0:
                lst[0].append(i)
            elif c < 0:
                lst[1].append(i)

        k = ccw(p1,p2,loc2) < 0
        if lst[k]:
            flag = True

    if len(hull) != 1 and (inside1==1 or inside2==1):
        print("IMPOSSIBLE")
        continue

    if check(hull,(loc1,loc2)) and not flag:
        print(f'{dist(loc1,loc2)**0.5:.3f}')
        continue

    lst = [[],[]]
    for i in hull:
        c = ccw(loc1,loc2,i)
        if c > 0:
            lst[0].append(i)
        elif c < 0:
            lst[1].append(i)

    if len(lst[0]) < len(lst[1]):
        lst[0],lst[1] = lst[1],lst[0]

    if not lst[1] and not flag:
        print(f'{dist(loc1,loc2)**0.5:.3f}')
        continue

    r1 = circ(gen(sorted(lst[0] + [loc1,loc2])))
    r2 = circ(gen(sorted(lst[1] + [loc1,loc2])))

    res = min(r1,r2) - dist(loc1,loc2)**0.5
    print(f'{res:.3f}')