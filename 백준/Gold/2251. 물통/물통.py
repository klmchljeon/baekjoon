#물통 56:46
from collections import deque

def pour(s,e):
    t = min(tmp[s],d[e]-tmp[e])
    res = [tmp[i] for i in range(3)]
    res[s] -= t
    res[e] += t

    return res

a,b,c = map(int,input().split())
d = (a,b,c)

visit = [[[False]*(c+1) for _ in range(b+1)] for _ in range(a+1)]
visit[0][0][c] = True

queue = deque([(0,0,c)])
while queue:
    tmp = queue.popleft()

    for i in range(3):
        for j in range(3):
            if i==j: continue

            if tmp[i] and tmp[j]!=d[j]:
                nx,ny,nz = pour(i,j)
                if not visit[nx][ny][nz]:
                    visit[nx][ny][nz] = True
                    queue.append((nx,ny,nz))

res = []
for i in range(c+1):
    if c-i > b: continue
    if visit[0][c-i][i]:
        res.append(i)

print(*res)