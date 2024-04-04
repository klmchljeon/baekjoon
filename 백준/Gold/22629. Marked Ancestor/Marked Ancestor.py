import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def dfs(x):
    for nx in graph[x]:
        if mark[nx] == False:
            merge(nx,x)

        dfs(nx)

def merge(a,b):
    pa = find(a)
    pb = find(b)

    parent[pa] = pb

def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]

n,q = map(int,input().split())
p = [None]*2
for i in range(n-1):
    x = int(input())
    p.append(x)

graph = [[] for _ in range(n+1)]
for x in range(2,n+1):
    graph[p[x]].append(x)

mark = [False]*(n+1)
mark[1] = True

query = []
for _ in range(q):
    op,x = input().split()
    x = int(x)
    if op == 'M':
        if mark[x]: continue
        mark[x] = True

    query.append((op,x))

parent = list(range(n+1))
dfs(1)

res = 0
for op,x in query[::-1]:
    if op == 'M':
        merge(x,p[x])
    else:
        t = find(x)
        res += t

print(res)