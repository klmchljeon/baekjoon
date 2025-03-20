import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def dfs(x,depth):
    for nx in graph[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x] + 1
            dfs(nx,depth)

    return 

def visit(s):
    depth = [-1]*(n+1)
    depth[s] = 0
    dfs(s,depth)
    return depth

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

a,b = map(int,input().split())

fire = visit(a)
v = visit(b)

res = 0
for i in range(1,n+1):
    if fire[i] <= v[i]: continue

    res = max(res, v[i] + (fire[i]-v[i]-1)//2)

print(res + 1)