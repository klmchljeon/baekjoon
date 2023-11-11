#트리의 지름

import sys
sys.setrecursionlimit(int(10e5))
input = sys.stdin.readline

n = int(input())
d = [[] for _ in range(n+1)]
for _ in range(n):
    a, *v = map(int,input().split())

    edges = []
    for j in range(0,len(v)-2,2):
        edges.append([v[j],v[j+1]])

    d[a] = edges[:]

def dfs(r,dis):
    for i in d[r]:
        if not visit[i[0]]:
            depth = dis+i[1]
            visit[i[0]] = True
            result[i[0]] = depth
            dfs(i[0],depth)
            

visit = [False]*(n+1); visit[1] = True
result = [0]*(n+1)
dfs(1,0)

v = result.index(max(result))
visit = [False]*(n+1); visit[v] = True
result = [0]*(n+1)
dfs(v,0)
print(max(result))