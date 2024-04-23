import sys
input = sys.stdin.readline

def dfs(x,prev):
    global tmp
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx,x)

        elif prev != nx:
            tmp = False

c = 1
while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False]*(n+1)
    res = 0
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            tmp = True
            dfs(i,None)
            res += tmp

    Case = f"Case {c}:"
    if res == 0:
        print(f"{Case} No trees.")
    elif res == 1:
        print(f"{Case} There is one tree.")
    else:
        print(f"{Case} A forest of {res} trees.")

    c += 1