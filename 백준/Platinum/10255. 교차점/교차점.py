def cal(a,b):
    x = a[1]-b[1]
    y = -(a[0]-b[0])
    c = -a[0]*(b[1]-a[1]) + a[1]*(b[0]-a[0])
    return x,y,c

def conv(lst):
    return lst[:2],lst[2:]

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def intersect(l1,l2):
    p1,p2 = conv(l1)
    p3,p4 = conv(l2)

    ccw1 = ccw(p1,p2,p3)*ccw(p1,p2,p4)
    ccw2 = ccw(p3,p4,p1)*ccw(p3,p4,p2)

    if ccw1==0 and ccw2==0:
        if p1>p2: p1,p2 = p2,p1
        if p3>p4: p3,p4 = p4,p3
        return p3<=p2 and p1<=p4

    return ccw1<=0 and ccw2<=0

def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]

def mul(a,b,d):
    x = (a[0][0]*b[0] + a[0][1]*b[1])
    y = (a[1][0]*b[0] + a[1][1]*b[1])
    if x%d == 0 and y%d == 0:
        return x//d, y//d
    else:
        return x/d, y/d
    
def f(l1,l2):
    if not intersect(l1,l2):
        return 0,None

    a,b = sorted(conv(l1))
    c,d = sorted(conv(l2))
    if a==d or b==c:
        res = a if a==d else b
        return 1,tuple(res)

    p = [[],[]]
    q = []

    x,y,z = cal(a,b)
    p[0] = [x,y]
    q.append(z)

    x,y,z = cal(c,d)
    p[1] = [x,y]
    q.append(z)

    if det(p) == 0:
        return 4,None

    inv = [[p[1][1],-p[0][1]],[-p[1][0],p[0][0]]]
    res = mul(inv,q,det(p))
    return 1,res

def sol(lst):
    for i in lst:
        if i[0] == 4:
            return 4
        
    for i in lst:
        if i[0] != 0:
            break

    else:
        return 0
    
    tmp = []
    for i in lst:
        if i[0] == 1:
            tmp.append(i[1])

    if len(tmp) == 1:
        return 1
    
    st = set(tmp)
    return len(st)

t = int(input())
for case in range(t):
    a,b = conv(list(map(int,input().split())))
    l = list(map(int,input().split()))

    c = [a[0],b[1]]
    d = [b[0],a[1]]

    rect = [a+c,c+b,b+d,d+a]
    lst = []
    for i in rect:
        lst.append(f(i,l))

    print(sol(lst))