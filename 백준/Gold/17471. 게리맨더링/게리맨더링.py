#게리맨더링
from collections import deque
max_ = 10000

def check(l):
    res = [0,0]
    for i in (0,1):
        tmp = bfs(l,i)
        if not tmp: 
            return max_
        
        res[i] = tmp

    return abs(res[0]-res[1])

def bfs(ver,p):
    visit = [p^1]*(n+1)
    queue = deque([])

    for i in range(1,n+1):
        if ver[i] == p:
            visit[i] = p
            queue.append(i)
            break

    cnt = 0
    while queue:
        x = queue.popleft()

        cnt += cost[x]

        for nx in d[x]:
            if visit[nx] == p^1 and ver[nx] == p:
                visit[nx] = p
                queue.append(nx)

    if visit[1:] == ver[1:]:
        return cnt
    
    else:
        return 0

def dfs():
    if len(s) == n+1:
        lst.append(s[:])
        return 
    
    for i in (0,1):
        s.append(i)
        dfs()
        s.pop()

    return 

n = int(input())
cost = [0] + list(map(int,input().split()))

d = [[]]
for _ in range(n):
    _,*tmp = map(int,input().split())
    d.append(tmp)

lst = []
s = [None]
dfs()

res = max_
for i in lst:
    res = min(res,check(i))

print(res if res!=max_ else -1)