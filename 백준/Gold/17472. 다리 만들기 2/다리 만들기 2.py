#다리 만들기 2
from collections import deque
max_ = 101

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    
    elif pa > pb:
        parent[pa] = pb

def bfs(loc):
    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m): continue
            if not land[nx][ny] and d[nx][ny]:
                land[nx][ny] = num
                queue.append((nx,ny))

    return 1

f = lambda x:x[2]

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

land = [[0]*m for _ in range(n)]
num = 1
for i in range(n):
    for j in range(m):
        if not land[i][j] and d[i][j]:
            land[i][j] = num
            num += bfs((i,j))

edge = [[max_]*(num) for _ in range(num)]
for i in range(n):
    prev = [None,0]
    for j in range(m):
        if land[i][j]:
            if prev[0] in (None,land[i][j]):
                prev = [land[i][j],0]

            else:
                a = prev[0]
                b = land[i][j]

                if prev[1] != 1:
                    edge[a][b] = min(edge[a][b],prev[1])
                    edge[b][a] = min(edge[a][b],prev[1])

                prev = [land[i][j],0]

        else:
            if prev[0] != None:
                prev[1] += 1

for j in range(m):
    prev = [None,0]
    for i in range(n):
        if land[i][j]:
            if prev[0] in (None,land[i][j]):
                prev = [land[i][j],0]

            else:
                a = prev[0]
                b = land[i][j]

                if prev[1] != 1:
                    edge[a][b] = min(edge[a][b],prev[1])
                    edge[b][a] = min(edge[a][b],prev[1])

                prev = [land[i][j],0]

        else:
            if prev[0] != None:
                prev[1] += 1

e = []
for i in range(1,num):
    for j in range(1,num):
        if edge[i][j] != max_:
            e.append((i,j,edge[i][j]))

e.sort(key = f)

parent = [i for i in range(num)]

res = 0
for a,b,c in e:
    if find(a)==find(b):
        continue

    merge(a,b)
    res += c

tmp = find(1)
for i in range(2,num):
    if tmp != find(i):
        print(-1)
        break

else:
    print(res)