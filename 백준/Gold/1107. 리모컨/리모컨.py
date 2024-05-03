#리모컨
from collections import deque

n = int(input())
m = int(input())
dir = set(map(str,range(10)))
if m: dir -= set(input().split())

ans = abs(n-100)

visit = [False]*(1000001)
zerovisit = {'0'*i:False for i in range(1,8)}
queue = deque([])
for i in dir:
    queue.append((i,1))

while queue:
    x,c = queue.popleft()

    ans = min(ans, abs(n-int(x))+c)

    for i in dir:
        nx = x+i
        temp = int(nx)

        if 0<=temp<=1000000 and not visit[temp]:
            visit[temp] = True
            queue.append((nx,c+1))

print(ans)