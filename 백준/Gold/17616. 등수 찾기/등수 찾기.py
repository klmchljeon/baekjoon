import sys
from collections import deque
input = sys.stdin.readline

n,m,x = map(int,input().split())

lst = []
for _ in range(m):
    a,b = map(int,input().split())
    lst.append((a,b))

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for a,b in lst:
    graph[a].append(b)
    degree[b] += 1

check = [False]*(n+1)
queue = deque([])
for i in range(1,n+1):
    if degree[i] == 0:
        queue.append(i)

check[x] = True
while queue:
    k = queue.popleft()

    for i in graph[k]:
        check[i] |= check[k]

        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

v = n - check.count(True) + 1

del graph
del degree
del check

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for a,b in lst:
    graph[b].append(a)
    degree[a] += 1

check = [False]*(n+1)
queue = deque([])
for i in range(1,n+1):
    if degree[i] == 0:
        queue.append(i)

check[x] = True
while queue:
    k = queue.popleft()

    for i in graph[k]:
        check[i] |= check[k]

        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

u = check.count(True)
print(u,v)