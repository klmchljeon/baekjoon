import sys
from collections import deque
input = sys.stdin.readline

n,m,x = map(int,input().split())

graph = [[[] for _ in range(n+1)] for _ in range(2)]
degree = [[0]*(n+1) for _ in range(2)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[0][a].append(b)
    degree[0][b] += 1

    graph[1][b].append(a)
    degree[1][a] += 1


check = [[False]*(n+1) for _ in range(n)]
for d in range(2):
    queue = deque([])
    for i in range(1,n+1):
        if degree[d][i] == 0:
            queue.append((i,i==x))

    check[d][x] = True
    while queue:
        k,p = queue.popleft()

        for i in graph[d][k]:
            check[d][i] |= check[d][k]

            degree[d][i] -= 1
            if degree[d][i] == 0:
                queue.append((i,p|(i==x)))

v = n - check[0].count(True) + 1
u = check[1].count(True)
print(u,v)