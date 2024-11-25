def conv(lst):
    return lst[:2],lst[2:]

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def area(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

def check(p):
    tmp = []
    for i in range(3):
        tmp.append(ccw(tr[i],tr[(i+1)%3],p))

    tmp.sort()
    return tmp[0]*tmp[2] >= 0

tr = []
for i in range(3):
    x,y = map(int,input().split())
    tr.append((x,y))

n = int(input())
lst = []
for i in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

a = area(*tr)
cnt = 0
for i in range(n):
    cnt += check(lst[i])

print(a)
print(cnt)