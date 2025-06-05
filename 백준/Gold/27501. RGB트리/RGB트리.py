import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(6e5))

def dfs(x):
    p = []
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx)
            p.append(nx)

    if not p:
        dp[x] = lst[x][:]
        return
    
    path[x].append(p)
    for i in range(3):
        val = 0
        tmp = []
        for nx in p:
            m = -1
            idx = -1
            for j in range(3):
                if i==j: continue
                if m < dp[nx][j]:
                    m = dp[nx][j]
                    idx = j+1

            val += m
            tmp.append(idx)

        dp[x][i] = lst[x][i] + val
        path[x].append(tmp)

    return

def f(x,idx):
    if not path[x]: return

    p = path[x][0]
    for i in range(len(p)):
        nx = p[i]
        nidx = path[x][idx][i]

        res[nx] = dic[nidx]
        f(nx,nidx)

    return

dic = dict(zip((1,2,3),'RGB'))

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

lst = [[]]
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

dp = [[-1]*3 for _ in range(n+1)]
path = [[] for _ in range(n+1)]
visited = [False]*(n+1)

visited[1] = True
dfs(1)


res = ['']*(n+1)

val = -1
idx = -1
for i in range(3):
    if val < dp[1][i]:
        val = dp[1][i]
        idx = i+1

res[1] = dic[idx]
f(1,idx)

print(max(dp[1]))
print(''.join(res))