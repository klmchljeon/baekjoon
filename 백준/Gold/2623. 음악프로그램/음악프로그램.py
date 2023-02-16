#음악 프로그램

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
d = [[] for i in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    k, *lst = map(int,input().split())
    for i in range(k-1):
        d[lst[i]].append(lst[i+1])
        degree[lst[i+1]] += 1

result = []
queue = deque()
for i in range(1,n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    result.append(x)

    for i in d[x]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

if len(result) != n:
    print(0)
else:
    print(*result,sep='\n')