import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

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

n,m,t = map(int,input().split())
lst = []
for _ in range(m):
    u,v,s = map(int,input().split())
    lst.append((s,u,v))

lst.sort()

parent = [i for i in range(n+1)]

res = 0
cnt = n
cur = 1
for s,u,v in lst:
    res += (s-cur)*cnt

    if find(u) != find(v):
        cnt -= 1
        merge(u,v)

    cur = s

res += (t+1-cur)*cnt

print(res)