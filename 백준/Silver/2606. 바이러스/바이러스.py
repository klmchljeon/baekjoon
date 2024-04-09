def dfs(x):
    for nx in graph[x]:
        if visited[nx] == False:
            visited[nx] = True
            dfs(nx)

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False]*(n+1)
visited[1] = True
dfs(1)

cnt = 0
for i in range(1,n+1):
    if visited[i] == True:
        cnt += 1
        
print(cnt-1)