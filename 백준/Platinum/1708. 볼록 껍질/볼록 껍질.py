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


n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
d.sort()

hull = []
hull += convex(d)
hull += convex(d[::-1])
print(len(hull))