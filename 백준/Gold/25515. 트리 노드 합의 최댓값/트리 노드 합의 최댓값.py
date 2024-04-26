import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def dfs(x):
    tmp = 0
    for nx in graph[x]:
        dfs(nx)
        tmp = max(tmp, tmp+dp[nx])

    dp[x] = lst[x] + tmp
    return 

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    p,c = map(int,input().split())
    graph[p].append(c)

lst = list(map(int,input().split()))

dp = [0]*n
dfs(0)

print(dp[0])