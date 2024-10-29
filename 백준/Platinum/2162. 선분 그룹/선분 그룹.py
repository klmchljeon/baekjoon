def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    elif pa > pb:
        parent[pa] = pb

def conv(lst):
    return lst[:2],lst[2:]

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def intersect(l1,l2):
    p1,p2 = conv(l1)
    p3,p4 = conv(l2)

    ccw1 = ccw(p1,p2,p3)*ccw(p1,p2,p4)
    ccw2 = ccw(p3,p4,p1)*ccw(p3,p4,p2)

    if ccw1==0 and ccw2==0:
        if p1>p2: p1,p2 = p2,p1
        if p3>p4: p3,p4 = p4,p3
        return p3<=p2 and p1<=p4

    return ccw1<=0 and ccw2<=0

n = int(input())
lst = []
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    lst.append((x1,y1,x2,y2))

parent = [i for i in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if intersect(lst[i],lst[j]):
            merge(i,j)

dic = dict()
for i in range(n):
    pi = find(i)
    if not pi in dic:
        dic[pi] = 0

    dic[pi] += 1

res = [0,0]
for i in dic:
    res[0] += 1
    res[1] = max(res[1],dic[i])

print(*res,sep='\n')