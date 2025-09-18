def dfs(x):
    tmp = []
    for nx in graph[x]:
        tmp.append(dfs(nx))

    tmp.sort(reverse = True)

    res = 0
    for i in range(len(tmp)):
        res = max(res,tmp[i]+i+1)

    dp[x] = res
    return dp[x]

n = int(input())
lst = list(map(int,input().split()))

graph = [[] for _ in range(n)]
for x in range(1,n):
    graph[lst[x]].append(x)

dp = [0]*n

print(dfs(0))