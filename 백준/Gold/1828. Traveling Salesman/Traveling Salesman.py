from collections import deque

def bfs(s,e):
    visited = [-1]*(n+1)
    visited[s] = 0

    queue = deque([s])
    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

    return visited[e]

n = int(input())
graph = [[] for _ in range(n+1)]
dic = dict()
for i in range(1,n+1):
    m,*tmp = map(int,input().split())
    lst = []
    for j in range(m):
        lst.append(tuple(tmp[3*j:3*j+3]))

    for j in range(m):
        a,b = lst[j],lst[(j+1)%m]
        if a > b:
            a,b = b,a

        if not (a,b) in dic:
            dic[(a,b)] = i
            continue

        p = dic[(a,b)]
        graph[i].append(p)
        graph[p].append(i)

q = int(input())
for _ in range(q):
    a,b = map(int,input().split())
    print(bfs(a,b))