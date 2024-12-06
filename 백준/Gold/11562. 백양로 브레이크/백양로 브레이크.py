import sys
input = sys.stdin.readline
inf = int(1e9)

n,m = map(int,input().split())
graph = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,b = map(int,input().split())
    graph[u][v] = 0
    graph[v][u] = b^1

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

k = int(input())
for _ in range(k):
    s,e = map(int,input().split())
    print(graph[s][e])