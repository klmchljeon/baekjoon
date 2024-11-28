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
        while len(res) >= 2 and ccw(res[-2],res[-1],i) <= 0:
            res.pop()
        res.append(i)

    res.pop()
    return res

def gen(lst):
    if len(lst) < 3:
        return lst
    
    lst.sort()
    res = convex(lst) + convex(lst[::-1])
    return res

n = int(input())
lst = []
for i in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

hull = gen(lst)
p = len(hull)

res = 0
for i in range(p):
    res += hull[i][0]*hull[(i+1)%p][1] - hull[i][1]*hull[(i+1)%p][0]

print(res//100)