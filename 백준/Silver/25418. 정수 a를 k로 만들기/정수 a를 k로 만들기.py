from collections import deque

max_ = int(1e6)
a,k = map(int,input().split())

visited = [-1]*(max_+1)
visited[a] = 0

queue = deque([a])
while queue:
    x = queue.popleft()

    for dx in (1,x):
        nx = x + dx
        if not (nx<max_+1): continue
        if visited[nx] == -1:
            visited[nx] = visited[x] + 1
            queue.append(nx)

print(visited[k])