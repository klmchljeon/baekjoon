#효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    d[b].append(a)

res = [[],0]
for i in range(1,n+1):
    visit = [False]*(n+1)
    visit[i] = True
    
    cnt = 1
    queue = deque([i])
    while queue:
        x = queue.popleft()

        for nx in d[x]:
            if not visit[nx]:
                visit[nx] = True
                queue.append(nx)
                cnt += 1

    if res[1] < cnt:
        res = [[i],cnt]
    
    elif res[1] == cnt:
        res[0].append(i)

print(*res[0])