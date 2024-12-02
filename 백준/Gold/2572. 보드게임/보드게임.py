import sys
input = sys.stdin.readline

n = int(input())
lst = input().split()

m,k = map(int,input().split())
graph = [[] for _ in range(m+1)]
for _ in range(k):
    a,b,c = input().split()
    a,b = map(int,(a,b))
    graph[a].append((b,c))
    graph[b].append((a,c))

dp = [[-1]*(m+1) for _ in range(n+1)]
dp[0][1] = 0
for i in range(n):
    for x in range(1,m+1):
        if dp[i][x] == -1: continue
        dp[i+1][x] = max(dp[i+1][x],0)

        for nx,c in graph[x]:
            dp[i+1][nx] = max(dp[i+1][nx], dp[i][x] + (c==lst[i]))

print(max(dp[n])*10)