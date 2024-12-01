import sys
input = sys.stdin.readline

def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

w = 0.1
n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

cx = 0
cy = 0
for x,y in lst:
    cx += x
    cy += y

cx /= n
cy /= n

w = 0.1
for _ in range(100000):
    d = 0
    m = -1
    for i in range(n):
        cur = dist((cx,cy),lst[i])
        if d < cur:
            d = cur
            m = i

    cx += (lst[m][0]-cx) * w
    cy += (lst[m][1]-cy) * w
    w *= 0.9995

print(f'{2*d:.2f}')