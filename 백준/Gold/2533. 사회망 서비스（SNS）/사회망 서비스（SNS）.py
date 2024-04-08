#사회망 서비스(SNS)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e6))
inf = int(1e6)+1

def dfs(x):
    tmp = []
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            tmp.append(nx)
            dfs(nx)

    for i in tmp:
        dp[x][0] += min(dp[i])
        dp[x][1] += dp[i][0]

    return 

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[1,0] for _ in range(n+1)]
visited = [False]*(n+1)
visited[1] = True
dfs(1)

print(min(dp[1]))