import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def dfs(x):
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dp[x] += dfs(nx) 

    return dp[x]

n,r,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [1]*(n+1)

visited = [False]*(n+1)
visited[r] = True
dfs(r)

for _ in range(q):
    u = int(input())
    print(dp[u])