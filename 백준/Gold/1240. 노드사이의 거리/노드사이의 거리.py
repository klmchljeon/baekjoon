def dfs(x):
    stack = [x]
    while stack:
        x = stack.pop()

        for nx,c in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + c
                stack.append(nx)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for _ in range(m):
    a,b = map(int,input().split())
    visited = [-1]*(n+1)
    visited[a] = 0
    dfs(a)

    print(visited[b])