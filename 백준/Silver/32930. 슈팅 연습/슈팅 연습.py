def dist(a):
    x1,y1 = a
    x2,y2 = cloc
    return (x1-x2)**2 + (y1-y2)**2

cloc = (0,0)

n,m = map(int,input().split())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

res = 0
for _ in range(m):
    tmp = -1
    idx = -1
    for i in range(n):
        p = dist(lst[i])
        if tmp < p:
            tmp = p
            idx = i

    res += tmp
    cloc = lst.pop(idx)

    x,y = map(int,input().split())
    lst.append((x,y))

print(res)