import sys
input = sys.stdin.readline

def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(pa,pb):
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

f = lambda x:(x[2])

t = int(input())
for case in range(t):
    n,m,p,q = map(int,input().split())
    if p > q: p,q = q,p

    edge = []
    for _ in range(m):
        u,v,w = map(int,input().split())
        if u > v: u,v = v,u

        edge.append((u,v,w))

    edge.sort(key = f)

    parent = list(range(n+1))
    flag = False
    for u,v,w in edge:
        pu = find(u)
        pv = find(v)
        if pu == pv: continue

        merge(pu,pv)
        flag |= (u,v)==(p,q)

    print('YES' if flag else "NO")