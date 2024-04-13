import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x):
    for nx in graph[x]:
        if depth[nx]==-1:
            depth[nx] = depth[x] + 1
            prev[nx] = x
            dfs(nx)

t = int(input())
for case in range(t):
    n = int(input())
    p = []

    graph = [[] for _ in range(n+1)]
    prev = [0]*(n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        prev[b] = a

    for i in range(1,n+1):
        if prev[i] == 0:
            root = i
            break

    depth = [-1]*(n+1)
    depth[root] = 0
    dfs(root)

    a,b = map(int,input().split())
    while depth[a]!=depth[b]:
        if depth[a] < depth[b]:
            b = prev[b]
        else:
            a = prev[a]

    while a!=b:
        a = prev[a]
        b = prev[b]

    print(a)
