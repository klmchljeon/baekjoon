#세부
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,tar,w):
    visit = [False]*(n+1)
    visit[x] = True

    queue = deque([x])
    while queue:
        x = queue.popleft()
        
        if x == tar:
            return True

        for nx,c in d[x]:
            if not visit[nx] and c >= w:
                visit[nx] = True
                queue.append(nx)

    return False

n,m = map(int,input().split())
u,v = map(int,input().split())
d = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

s,e = 0,int(1e9)+1
while s+1<e:
    mid = (s+e)//2
    
    if bfs(u,v,mid):
        s = mid

    else:
        e = mid

print(s)