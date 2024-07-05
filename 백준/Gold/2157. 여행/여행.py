import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(k):
    a,b,c = map(int,input().split())
    if a > b: continue

    graph[a].append((b,c))

dp = [[0]*m for _ in range(n+1)]
for x in range(1,n):
    for j in range(m-1):
        if dp[x][j] == 0 and x != 1: continue

        for nx,c in graph[x]:
            dp[nx][j+1] = max(dp[nx][j+1], dp[x][j] + c)

print(max(dp[n]))