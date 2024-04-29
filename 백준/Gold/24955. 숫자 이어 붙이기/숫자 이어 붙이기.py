import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
mod = int(1e9)+7

def l(num):
    res = 0
    while num:
        num //= 10
        res += 1

    return res

def dfs(x):
    for nx in graph[x]:
        if depth[nx]==-1:
            depth[nx] = depth[x] + 1
            parent[nx] = x
            dfs(nx)

n,q = map(int,input().split())
lst = [0]+list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [-1]*(n+1)
depth[1] = 0

parent = [0]*(n+1)
dfs(1)

for _ in range(q):
    x,y = map(int,input().split())
    numx, numy = 0,0
    leny = 1
    while depth[x]!=depth[y]:
        if depth[x] > depth[y]:
            numx = (numx*10**l(lst[x]) + lst[x])%mod
            x = parent[x]

        else:
            numy = (lst[y]*leny + numy)%mod
            leny = (leny * 10**l(lst[y]))%mod
            y = parent[y]

    while x!=y:
        numx = (numx*10**l(lst[x]) + lst[x])%mod
        x = parent[x]
        numy = (lst[y]*leny + numy)%mod
        leny = (leny * 10**l(lst[y]))%mod
        y = parent[y]

    numx = (numx*10**l(lst[x]) + lst[x])%mod

    res = (numx*leny + numy)%mod
    print(res)