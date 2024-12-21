import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa

    elif pa > pb:
        parent[pa] = pb

n,m = map(int,input().split())
edge = []
for _ in range(m+1):
    a,b,c = map(int,input().split())
    edge.append((c^1,a,b))

edge.sort()

parent = list(range(n+1))
res1 = 0
cnt = 0
for c,a,b in edge:
    pa = find(a)
    pb = find(b)
    if pa == pb: continue

    merge(a,b)
    res1 += c
    cnt += 1
    if cnt == n: break

parent = list(range(n+1))
res2 = 0
cnt = 0
for c,a,b in edge[::-1]:
    pa = find(a)
    pb = find(b)
    if pa == pb: continue

    merge(a,b)
    res2 += c
    cnt += 1
    if cnt == n: break

print(res2**2-res1**2)