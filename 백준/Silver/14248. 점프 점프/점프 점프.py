#점프 점프
from collections import deque

n = int(input())
d = list(map(int,input().split()))
s = int(input()) - 1

cnt = 0

visit = [False]*n
visit[s] = True

queue = deque([s])
while queue:
    x = queue.popleft()
    cnt += 1

    for i in (-1,1):
        nx = x + i*d[x]
        if 0<=nx<n and not visit[nx]:
            visit[nx] = True
            queue.append(nx)

print(cnt)