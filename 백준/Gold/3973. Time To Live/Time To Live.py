from collections import deque

def bfs(v):
    depth = [-1]*n
    depth[v] = 0

    queue = deque([v])
    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if depth[nx] == -1:
                depth[nx] = depth[x] + 1
                queue.append(nx)

    res = (-1,None)
    for i in range(n):
        if res[0] < depth[i]:
            res = (depth[i],i)

    return res

t = int(input())
for case in range(t):
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    p = bfs(bfs(0)[1])[0]
    print(p//2 + p%2)