import sys
input = sys.stdin.readline

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def convex(lst):
    res = []
    for loc,i in lst:
        if visited[i]: continue

        while len(res) >= 2 and ccw(res[-2][0],res[-1][0],loc) < 0:
            res.pop()
        res.append((loc,i))

    return res

def gen(lst):
    if len(lst) < 3:
        return lst
    
    lst.sort()
    res = convex(lst) + convex(lst[::-1])
    return res

n,x,y = map(int,input().split())
lst = [((x,y),0)]
for i in range(1,n+1):
    x,y = map(int,input().split())
    lst.append(((x,y),i))

visited = [False]*(n+1)
cnt = 0
while True:
    tmp = gen(lst)
    for _,i in tmp:
        visited[i] = True

    if visited[0]: break

    cnt += 1

print(cnt)