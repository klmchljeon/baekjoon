def enclosing_circle(a,b,c):
    ax,ay = a
    bx,by = b
    cx,cy = c

    d = 2*(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
    if d == 0: return None

    x = 1/d * ((ax**2 + ay**2)*(by-cy) + (bx**2 + by**2)*(cy-ay) + (cx**2 + cy**2)*(ay-by))
    y = 1/d * ((ax**2 + ay**2)*(cx-bx) + (bx**2 + by**2)*(ax-cx) + (cx**2 + cy**2)*(bx-ax))

    return (x,y)

def mid(a,b):
    return (a[0]+b[0])/2,(a[1]+b[1])/2

def inside(c,a,p):
    return dist(c,a) >= dist(c,p)

def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

n = int(input())
lst = []
for _ in range(n):
    x,y = map(float,input().split())
    lst.append((x,y))

res = int(1e9)
loc = None
for i in range(n-1):
    for j in range(i+1,n):
        circle = mid(lst[i],lst[j])
        for k in range(n):
            if k in (i,j): continue

            if not inside(circle,lst[i],lst[k]):
                tmp = enclosing_circle(lst[i],lst[j],lst[k])
                if tmp != None:
                    circle = tmp

        for k in range(n):
            if not inside(circle,lst[i],lst[k]):
                break

        else:
            d = dist(circle,lst[i])**0.5
            if res > d:
                res = d
                loc = circle

print(*loc,res)