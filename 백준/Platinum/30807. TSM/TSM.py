import sys
input = sys.stdin.readline

def find(p,x):
    if p[x] == x: return x
    p[x] = find(p,p[x])
    return p[x]

def merge(p,pa,pb):
    if pa < pb:
        p[pb] = pa

    elif pa > pb:
        p[pa] = pb

def check(num):
    edge = gen(num)
    return mst(edge) >= k

def gen(num):
    edge = []
    for i in range(m):
        a,b,c,d = lst[i]
        if num:
            tmp = min(d-c,num)
            c += tmp
            num -= tmp

        edge.append((c,a,b))

    return edge

def mst(edge):
    edge.sort()
    parent = list(range(n+1))

    cnt = 0
    cost = 0
    for c,a,b in edge:
        pa = find(parent,a)
        pb = find(parent,b)
        if pa == pb: continue

        merge(parent,pa,pb)
        cnt += 1
        cost += c

        if cnt == n-1:
            return cost
        
    raise AssertionError

n,m,k = map(int,input().split())
lst = []

s,e = -1,1
for _ in range(m):
    a,b,c,d = map(int,input().split())
    lst.append((a,b,c,d))

    e += d-c

if not (mst(gen(0)) <= k <= mst(gen(e))):
    print('NO')
    exit()

while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

edge = gen(e)
print('YES')
for c,*_ in edge:
    print(c)