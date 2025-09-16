import sys
input = sys.stdin.readline

def cp(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)

def ip(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x2-x1)*(x3-x2) + (y2-y1)*(y3-y2)

def dist_line(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    k = abs((y1-y2)*x3 - (x1-x2)*y3 + y1*(x1-x2) - x1*(y1-y2))
    return k / dist(p1,p2)

def dist(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

xa,ya,xb,yb = map(int,input().split())
a = (xa,ya)
b = (xb,yb)
c = (xa+(xa-xb), ya+(ya-yb))

r = dist(a,b)

res = 0
for p in lst:
    if cp(a,b,p) >= 0:
        d = max(0, dist(p,a) - r)

    else:
        if ip(b,c,p) > 0:
            d = dist(p,c)

        elif ip(c,b,p) > 0:
            d = dist(p,b)

        else:
            d = dist_line(a,b,p)

    res += d

print(res)