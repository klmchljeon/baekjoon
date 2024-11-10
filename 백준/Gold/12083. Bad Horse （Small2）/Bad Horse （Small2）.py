from collections import deque

def bfs(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x]^1
                queue.append(nx)

            elif not visited[nx]^visited[x]:
                return False

    return True

t = int(input())
for case in range(t):
    m = int(input())
    
    graph = [[] for _ in range(2*m)]
    dic = dict()
    for _ in range(m):
        a,b = input().split()
        for i in (a,b):
            if not i in dic:
                dic[i] = len(dic)

        graph[dic[a]].append(dic[b])
        graph[dic[b]].append(dic[a])

    n = len(dic)
    visited = [-1]*n
    for i in range(n):
        if visited[i] != -1: continue

        visited[i] = 0
        if not bfs(i):
            res = 'No'
            break

    else:
        res = 'Yes'

    print(f'Case #{case+1}: {res}')