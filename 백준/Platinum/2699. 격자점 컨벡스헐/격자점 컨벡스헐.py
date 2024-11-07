#볼록 껍질
import sys
input = sys.stdin.readline

ccw = lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])
def convex(lst):
    res = []
    for i in lst:
        while len(res) >= 2 and ccw(*res[-2:],i) <= 0:
            res.pop()
        res.append(i)

    res.pop()
    return res

t = int(input())
for case in range(t):
    n = int(input())
    d = []
    for _ in range((n//5) + bool(n%5)):
        tmp = list(map(int,input().split()))
        for i in range(0,len(tmp),2):
            d.append((tmp[i],tmp[i+1]))

    d.sort()

    hull = []
    hull += convex(d)
    hull += convex(d[::-1])

    hull = hull[::-1]
    p = hull[0]
    idx = 0
    for i in range(len(hull)):
        if p[1] < hull[i][1]:
            p = hull[i]
            idx = i

        elif p[1] == hull[i][1] and p[0] > hull[i][0]:
            p = hull[i]
            idx = i

    m = len(hull)
    print(m)
    for i in range(m):
        print(*hull[(idx+i)%m])