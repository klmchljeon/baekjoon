from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

x = 1
visited = [-1]*(n+1)
visited[x] = 0

queue = deque([x])
while queue:
    x = queue.popleft()

    for nx,c in graph[x]:
        if visited[nx] == -1:
            visited[nx] = visited[x] + c
            queue.append(nx)

print(max(visited))