import sys
from math import pi,sin,cos
input = sys.stdin.readline

def ccw(a1, b1, a2, b2, a3, b3):
    s = (a1*b2 + a2*b3 + a3*b1) - (a2*b1 + a3*b2 + a1*b3)
    
    if s > 0: return 1
    elif s == 0: return 0
    else: return -1
    
def inter(x1,y1,x2,y2,x3,y3,x4,y4):
    flagA = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    flagB = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    
    if flagA == 0 and flagB == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
            return 1
        else:
            return 0
    else:
        if flagA <= 0 and flagB <= 0:
            return 1
        else:
            return 0

def convt(p,t):
    m = (p-t)/1800 * pi
    return 1000*cos(m),1000*sin(m)

n = int(input())
lst = []
lst2 = []
for _ in range(n):
    a,b = map(int,input().split())
    if abs(a-b) == 1800:
        lst2.append(a)
        lst2.append(b)
    else:
        lst.append((a,b))

lst2.sort()

p1 = tuple(map(int,input().split()))
p2 = tuple(map(int,input().split()))

cnt1 = 0
for i in lst2:
    if p1[0] > i:
        cnt1 += 1

    else:
        break

for a,b in lst:
    q1 = convt(a,p1[0])
    q2 = convt(b,p1[0])

    if inter(*q1,*q2,0,0,p1[1],0):
        cnt1 += 1

cnt2 = 0
for i in lst2:
    if p2[0] > i:
        cnt1 += 1

    else:
        break

for a,b in lst:
    q1 = convt(a,p2[0])
    q2 = convt(b,p2[0])

    if inter(*q1,*q2,0,0,p2[1],0):
        cnt2 += 1

print('YES' if cnt1%2 == cnt2%2 else 'NO')
