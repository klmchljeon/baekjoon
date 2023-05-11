#강아지는 많을수록 좋다
import sys
from collections import deque
input = sys.stdin.readline

n,m,a,b = map(int,input().split())
visit = [-1]*(n+1)

for _ in range(m):
    l,r = map(int,input().split())
    for i in range(l,r+1):
        visit[i] = 0

visit[0] = 0
queue = deque([0])
while queue:
    x = queue.popleft()

    for i in (a,b):
        nx = x + i
        if nx<=n and visit[nx]==-1:
            visit[nx] = visit[x] + 1
            queue.append(nx)

print(visit[n])