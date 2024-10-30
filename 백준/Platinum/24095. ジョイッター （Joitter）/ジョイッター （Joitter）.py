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

n = int(input())
lst = [int(input()) for _ in range(n)]
graph = [list(map(int,input().split())) for _ in range(n)]

if 1 in lst:
    cnt = 0
    res = 0
    for i in range(n):
        if lst[i] != 1: continue
        for j in range(n):
            if i == j: continue
            if i < j and lst[j] == 1: continue

            cnt += 1
            res += graph[i][j]

    print(cnt,res)
    exit()

if not 2 in lst:
    parent = [i for i in range(n)]
    edge = []
    for i in range(n):
        for j in range(i+1,n):
            edge.append((graph[i][j],i,j))

    edge.sort()

    cnt = 0
    res = 0
    for c,a,b in edge:
        if find(a) != find(b):
            merge(a,b)
            cnt += 1
            res += c

            if cnt == n-1: break

    print(cnt,res)
    exit()

cnt = n-1
res = int(1e18)
if lst.count(2) == 2:
    p = [i for i in range(n) if lst[i] == 2]
    tmp = graph[p[0]][p[1]]
    for i in range(n):
        tmp += min(graph[i][p[0]],graph[i][p[1]])

    res = min(res,tmp)

for i in range(n):
    tmp = 0
    for j in range(n):
        if i==j: continue

        tmp += graph[i][j]

    res = min(res,tmp)

print(cnt,res)