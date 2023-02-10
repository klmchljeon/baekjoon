#중량제한
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def bfs(x,tar,w):
    visit = [False]*(n+1)
    visit[x] = True

    queue = deque([x])
    while queue:
        x = queue.popleft()
        
        if x == tar:
            return True

        for nx in dic[x]:
            if not visit[nx] and dic[x][nx] >= w:
                visit[nx] = True
                queue.append(nx)

    return False

n,m = map(int,input().split())
dic = [defaultdict(int) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    dic[a][b] = max(dic[a][b],c)
    dic[b][a] = max(dic[b][a],c)

u,v = map(int,input().split())

s,e = 1,int(1e9)+1
while s+1<e:
    mid = (s+e)//2
    
    if bfs(u,v,mid):
        s = mid

    else:
        e = mid

print(s)