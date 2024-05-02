import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    v = d[x]
    c = 1
    
    queue = deque([x])
    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                v += d[nx]
                c += 1
                queue.append(nx)

    return v,c

n,m,k = map(int,input().split())
d = [0] + list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

val = [0]
cnt = [0]

visited = [False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        visited[i] = True
        tmp = bfs(i)
        val.append(tmp[0])
        cnt.append(tmp[1])

n_ = len(val)-1
dp = [[0]*(k) for _ in range(n_+1)]
for i in range(1,n_+1):
    for j in range(1,k):
        if cnt[i] > j:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cnt[i]] + val[i])

print(dp[n_][k-1])