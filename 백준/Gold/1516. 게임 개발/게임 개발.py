#게임 개발
from collections import deque

n = int(input())
d = [[] for _ in range(n)]
degree = [0]*n

a = [0]*n
for i in range(n):
    s,*k = map(int,input().split())
    a[i] = s

    for j in k[:-1]:
        d[j-1].append(i)
        degree[i] += 1

queue = deque([])
for i in range(n):
    if not degree[i]:
        queue.append(i)

res = [0]*n
while queue:
    x = queue.popleft()
    res[x] += a[x]

    for nx in d[x]:
        degree[nx] -= 1
        res[nx] = max(res[nx],res[x])
        if not degree[nx]:
            queue.append(nx)

print(*res,sep='\n')