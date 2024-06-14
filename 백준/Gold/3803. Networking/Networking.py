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

while True:
    n,*m = map(int,input().split())
    if n == 0: break
    m = m[0]

    edge = []
    for _ in range(m):
        u,v,w = map(int,input().split())
        #if u > v: u,v = v,u

        edge.append((u,v,w))

    edge.sort(key = f)

    parent = list(range(n+1))
    res = 0
    for u,v,w in edge:
        pu = find(u)
        pv = find(v)
        if pu == pv: continue

        merge(pu,pv)
        res += w

    print(res)
    input()