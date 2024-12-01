import sys
input = sys.stdin.readline

def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)**0.5

while True:
    w = 0.1
    n = int(input())
    if not n: break

    lst = []
    for _ in range(n):
        x,y,z = map(float,input().split())
        lst.append((x,y,z))

    cx = 0
    cy = 0
    cz = 0
    for x,y,z in lst:
        cx += x
        cy += y
        cz += z

    cx /= n
    cy /= n
    cz /= n

    w = 0.1
    for _ in range(100000):
        d = 0
        m = -1
        for i in range(n):
            cur = dist((cx,cy,cz),lst[i])
            if d < cur:
                d = cur
                m = i

        cx += (lst[m][0]-cx) * w
        cy += (lst[m][1]-cy) * w
        cz += (lst[m][2]-cz) * w
        w *= 0.9997

    print(d)